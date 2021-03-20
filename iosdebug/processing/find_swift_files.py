import os


def find_swift_files():
    swift_files = []

    for directory, _, files in os.walk(os.getcwd()):
        for file in files:
            if file[-6:] == '.swift' and '.build' not in directory \
                    and 'Pods' not in directory and 'Tests' not in directory:
                swift_files.append(directory + os.sep + file)

    return swift_files
