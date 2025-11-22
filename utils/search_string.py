import os

def find_string_in_files(search_string, folder_path='.'):
    """
    Find files containing a specific string in a given folder.

    :param search_string: The string to search for.
    :param folder_path: The path to the folder to search in. Defaults to the current directory.
    :return: A list of file paths containing the string.
    """
    found_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    if search_string in f.read():
                        found_files.append(file_path)
            except (IOError, OSError):
                # Ignore files that can't be opened
                continue
    return found_files
