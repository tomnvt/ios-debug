from iosdebug.processing.starting.get_stored_mock_implementation import (
    get_stored_mock_implementation,
)
from iosdebug.templates import FUNCTION_TEMPLATE, TEMPLATE


def write_mock_implementations(
    repository_protocols, path_to_content_map, protocol_to_protocol_functions, root_path
):
    cases = ["Mocked1", "Mocked2", "Mocked3"]
    for protocol in repository_protocols:
        for path in path_to_content_map:
            if "class " + protocol in path_to_content_map[path]:
                stored_impl = get_stored_mock_implementation(root_path, protocol)
                if stored_impl and False:
                    processed_template = (
                        "// MARK: - Mock implementation\n" + stored_impl
                    )
                else:
                    functions = []
                    for function in protocol_to_protocol_functions[protocol]:
                        processed_func_template = FUNCTION_TEMPLATE
                        processed_func_template = processed_func_template.replace(
                            "<FUNC_NAME>", function.name
                        )
                        if function.generic_parameter_clause:
                            generic_param = function.generic_parameter_clause
                        else:
                            generic_param = ''
                        processed_func_template = processed_func_template.replace(
                            "<GENERIC_PARAMETER_CLAUSE>", generic_param
                        )
                        if function.params:
                            processed_func_template = processed_func_template.replace(
                                "<FUNC_PARAMS>", ", ".join(function.params)
                            )
                        else:
                            processed_func_template = processed_func_template.replace(
                                "<FUNC_PARAMS>", ""
                            )
                        processed_func_template = processed_func_template.replace(
                            "<CASES>",
                            "\n        ".join(
                                ['case "' + case + '": break' for case in cases]
                            ),
                        )
                        if function.params:
                            split_parameters = [
                                param.split(":")[0].split() for param in function.params
                            ]
                            arguments = []
                            for param_names in split_parameters:
                                if len(param_names) == 2:
                                    if param_names[0] == "_":
                                        arguments.append(param_names[1])
                                    else:
                                        arguments.append(
                                            param_names[0] + ": " + param_names[1]
                                        )
                                else:
                                    arguments.append(
                                        param_names[0] + ": " + param_names[0]
                                    )
                            func_call = "(" + ", ".join(arguments) + ")"
                        else:
                            func_call = "()"
                        processed_func_template = processed_func_template.replace(
                            "<ORIGINAL_FUNC_CALL>", function.name + func_call
                        )
                        if function.return_type:
                            processed_func_template = processed_func_template.replace(
                                "<RETURN_TYPE>", "-> " + function.return_type + " "
                            )
                            processed_func_template = processed_func_template.replace(
                                "<RETURN>", "return "
                            )
                        else:
                            processed_func_template = processed_func_template.replace(
                                "<RETURN_TYPE>", ""
                            )
                            processed_func_template = processed_func_template.replace(
                                "<RETURN>", ""
                            )

                        functions.append(processed_func_template)

                    processed_template = TEMPLATE
                    processed_template = processed_template.replace(
                        "<PROTOCOL>", protocol
                    )

                    processed_template = processed_template.replace(
                        "<FUNCTIONS>", "\n    ".join(functions)
                    )

                with open(path, "a") as file:
                    file.write(processed_template)
