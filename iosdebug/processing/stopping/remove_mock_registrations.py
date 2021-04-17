import re


def remove_mock_registrations(swift_files):
    container_builder_file = [
        file for file in swift_files if "ContainerBuilder.swift" in file
    ][0]
    with open(container_builder_file, "r") as file:
        content = file.read()
        repository_registration = re.findall(
            "static func registerRepository[\s\S]*?\n    \}", content
        )[0]
        repository_reg_rows = [
            row
            for row in repository_registration.split("\n")
            if "registerMock" not in row
        ]
        repository_registration_processed = "\n".join(repository_reg_rows)
    with open(container_builder_file, "w") as file:
        file.write(
            content.replace(repository_registration, repository_registration_processed)
        )
