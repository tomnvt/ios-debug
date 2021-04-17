import re


def find_repository_protocols(path_to_content_map):
    repository_protocols = []

    for file_path in path_to_content_map:
        content = path_to_content_map[file_path]
        repository_definition = re.findall("class .*Repository.*{[\s\S]*}", content)
        if repository_definition and "Mock" not in repository_definition[0]:
            protocol_conformance_row = re.findall(
                "extension (\w+)Impl: \\1 \{", repository_definition[0]
            )
            if protocol_conformance_row:
                repository_protocols.append(protocol_conformance_row[0])

    print("Found repository protocols:\n")
    _ = [print(repo) for repo in repository_protocols]
    return repository_protocols
