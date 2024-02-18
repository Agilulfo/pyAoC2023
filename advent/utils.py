import os


def input_path(script_path):
    directory_name = os.path.dirname(os.path.realpath(script_path))

    return os.path.join(directory_name, "input")
