import re

def is_debug_mode_on(swift_files):
    for file_path in swift_files:
        with open(file_path, "r") as file:
            if 'ShakableNavigationController' in file.read():
                return True

    return False