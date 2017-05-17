import os


def filename_cleaner(input_path, bad_chars, replacement_char="_", clean_type = "both", actually_rename=False):
    """
    Strips out and replaces undesirable characters from file and directory names.

    :param input_path: The path where you want to do the renaming (note that it recursively searches all
    subdirectories).
    :param bad_chars: Characters to strip out (can be a list or a string; if a string is provided, each character in
    the string will be treated separately).
    :param replacement_char: Character to replace the bad characters with.
    :param clean_type: "files" if you only want to rename files; "dirs" if you only want to rename directories; "both"
    if you want to rename both.
    :param actually_rename: True to actually rename the files or directories; false to just do a test run without
    renaming anything.

    Usage example:
    filename_cleaner(input_path = r"/home/user/test", bad_chars = '\/*?:"<>|', replacement_char = "_", 
    clean_type = "both", actually_rename = True)
    """

    # TODO: Validate input further
    if not os.path.exists(input_path):
        raise NotADirectoryError

    if clean_type == "files":
        clean_files = True
        clean_dirs = False
    elif clean_type == "dirs":
        clean_files = False
        clean_dirs = True
    elif clean_type == "both":
        clean_files = True
        clean_dirs = True
    else:
        raise Exception("Invalid clean_type, please use a valid value!")

    to_rename = {}
    for root, dirs, files in os.walk(input_path, topdown=False):
        if clean_dirs:
            for name in dirs:
                new_name = name
                for c in bad_chars:
                    new_name = new_name.replace(c, replacement_char)
                if new_name != name:
                    to_rename[os.path.join(root, name)] = os.path.join(root, new_name)
        if clean_files:
            for name in files:
                new_name = name
                for c in bad_chars:
                    new_name = new_name.replace(c, replacement_char)
                if new_name != name:
                    to_rename[os.path.join(root, name)] = os.path.join(root, new_name)

    print("Cleaning " + clean_type + "...")
    print("=" * 30)

    for name, new_name in to_rename:
        if actually_rename:
            os.rename(name, new_name)
            print("Renamed: " + name)
        else:
            print("Would have renamed: " + name)
        print("To: " + new_name)
        print("-" * 30)
    print("=" * 30)


if __name__ == "__main__":
    # TODO: If this module is run directly, run its tests using something like below
    # import test_fc
    # test_fc.run_tests()
    # TODO: Or merge in run_fc.py and convert this to a command-line tool
    pass
