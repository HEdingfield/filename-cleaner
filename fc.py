import os


def filename_cleaner(input_path, clean_type, bad_chars, replacement_char="_", actually_rename=False):
    """
    Strips out and replaces undesirable characters from filenames and directories.

    :param input_path: The path where you want to do the renaming (note that it recursively searches all
    subdirectories).
    :param clean_type: "dirs" if you want to rename directories and "files" if you want to rename files.
    :param bad_chars: Characters to strip out (can be a list or a string; if a string is provided, each character in
    the string will be treated separately).
    :param replacement_char: Character to replace the bad characters with.
    :param actually_rename: True to actually rename the files or directories; false to just do a test run without
    renaming anything.

    Usage example:
    filename_cleaner(input_path = r"/home/user/test", clean_type = "dirs", bad_chars = '\/*?:"<>|',
    replacement_char = "_", actually_rename = True)
    """

    # TODO: Validate input further
    if not os.path.exists(input_path):
    # if not Path(input_path).exists():
        raise NotADirectoryError

    print("Cleaning " + clean_type + "...")
    print("=" * 30)
    ndict = {'dirs': '', 'files': ''}
    for root, ndict['dirs'], ndict['files'] in os.walk(input_path, topdown=False):
        for name in ndict[clean_type]:
            newname = name
            for c in bad_chars:
                newname = newname.replace(c, replacement_char)
            if newname != name:
                path = os.path.join(root, name)
                newpath = os.path.join(root, newname)
                if actually_rename:
                    os.rename(path, newpath)
                    print("Renamed: " + path)
                else:
                    print("Would have renamed: " + path)
                print("To: " + newpath)
                print("-" * 30)
    print("=" * 30)


if __name__ == "__main__":
    # TODO: If this module is run directly, run its tests using something like below
    # import test_fc
    # test_fc.run_tests()
    # TODO: Or merge in run_fc.py and convert this to a command-line tool
    pass
