import pickle
import re
from ast import literal_eval

from iosdebug.constants import DATA_FILE
from iosdebug.templates import SHAKABLE_NC, SHAKABLE_NC_INSTANCE


def create_and_set_mock_manager(
    swift_files, path_to_content_map, processed_mock_manager
):
    for file_path in swift_files:
        with open(file_path, "r") as file:
            content = file.read()
            path_to_content_map[file_path] = content
            root_vc_property = re.findall(r"rootViewController[\s]+=[\s]+(.*)", content)
            if root_vc_property:
                if root_vc_property[0] == SHAKABLE_NC_INSTANCE:
                    break
                nav_con = "UINavigationController()"
                if root_vc_property[0] == nav_con:
                    root_vc_property_definition = nav_con
                    content = content.replace(nav_con, SHAKABLE_NC_INSTANCE)
                    changed = ""
                else:
                    root_vc_property_definition = re.findall(
                        root_vc_property[0] + " = .*", content
                    )[0]
                    root_vc_property_instance = re.findall(
                        " = (.*)", root_vc_property_definition
                    )[0]
                    changed = root_vc_property_definition.replace(
                        root_vc_property_instance, SHAKABLE_NC_INSTANCE
                    )
                    content = content.replace(root_vc_property_definition, changed)
                with open(file_path, "w") as file:
                    file.write(content)
                    if "/ MARK: - Debug mode helper classes" not in content:
                        file.write(SHAKABLE_NC)
                        file.write(processed_mock_manager)

                if "/ MARK: - Debug mode helper classes" not in content:
                    with open(DATA_FILE, "rb") as file:
                        data = pickle.load(file)
                        data = literal_eval(data)
                        data[
                            "original_root_view_controller"
                        ] = root_vc_property_definition
                        data["changed_root_view_controlbler"] = changed
                    with open(DATA_FILE, "wb") as file:
                        pickle.dump(str(data), file)
