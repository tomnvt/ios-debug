import iosdebug.logger as logger
import re


def add_mock_registrations_to_container_builder(swift_files, registrations):
    logger.instance.info('Looking for ContainerBuilder.swift file')
    try:
        container_builder_file = [file for file in swift_files if 'ContainerBuilder.swift' in file][0]
    except IndexError:
        logger.instance.error('ContainerBuilder.swift file not found')
    with open(container_builder_file, 'r') as file:
        content = file.read()
        registration_rows = '\n        '.join(registrations)
        repository_registration = re.findall('static func registerRepository[\s\S]*?\n    \}', content)[0]
        repository_registration_processed = repository_registration\
            .replace('return container', registration_rows + '\n        return container')

    if registration_rows not in content:
        with open(container_builder_file, 'w') as file:
            file.write(content.replace(repository_registration, repository_registration_processed))
