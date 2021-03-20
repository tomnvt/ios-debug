import os
import sys
from collections import namedtuple
from iosdebug.start import start
from iosdebug.stop import stop
from iosdebug.sync import sync
import iosdebug.logger as logger


Command = namedtuple('Command', 'name, description, execute')

commands = [
    Command('start', 'Stars debug mode', start),
    Command('stop', 'Stops debug mode', stop),
    Command('sync', 'Syncs mocked function', sync),
]


def get_selected_command():
    arguments = sys.argv
    if len(arguments) < 2:
        logger.instance.error('No command found')
        print('No command found. Please use one of the following:')
        _ = [print(command.name, '-', command.description) for command in commands]
        sys.exit(0)
    return arguments[1]


def try_command_execution(selected_command):
    logger.instance.info('Selected command: ' + selected_command)
    logger.instance.debug('Selected command: ' + selected_command)
    command_names = [command.name for command in commands]
    if selected_command in command_names:
        logger.instance.info('Executing command: ' + selected_command)
        print('Executing command:', selected_command)
        index = command_names.index(selected_command)
        commands[index].execute()
        os.remove(logger.LOG_FILE_NAME)
    else:
        logger.instance.logger.error('No command found')
        print('No command found. Please use one of the following:')
        _ = [print(command.name, '-', command.description) for command in commands]

def main():
    # setup_logger()
    selected_command = get_selected_command()
    try_command_execution(selected_command)


if __name__ == "__main__":
    main()
