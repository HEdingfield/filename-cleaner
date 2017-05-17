import unittest
from pathlib import Path
from fc import filename_cleaner


class Test(unittest.TestCase):
    def setUp(self):
        # Create temporary files and directories to test on
        self.input_path = Path.cwd().__str__() + "\\testing"
        if not Path(self.input_path).exists():
            Path(self.input_path).mkdir(parents=True)
        self.bad_chars = '\/*?:"<>|'
        self.replacement_char = "_"
        self.clean_type = "both"
        self.actually_rename = False

    def tearDown(self):
        # Delete all temporary files and directories created
        p = Path(self.input_path)
        for f in p.glob('**/*'):
            if f.is_file():
                f.unlink()
        p.rmdir()

    def test_bad_input_dir(self):
        input_path = self.input_path + "\\bad_path\\"
        self.assertRaises(NotADirectoryError, filename_cleaner, input_path, self.bad_chars, self.replacement_char,
                          self.clean_type, self.actually_rename)

    def test_no_rename(self):
        # Create files
        Path(self.input_path + '\\test1.txt').touch()
        Path(self.input_path + '\\t1est.t1xt').touch()
        Path(self.input_path + '\\test.txt').touch()
        # TODO: create files in subdirectories, some of which are renamed
        # TODO: create directories

        names_set_before = set([str(name) for name in Path(self.input_path).iterdir()])
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set_after = set([str(name) for name in Path(self.input_path).iterdir()])
        self.assertFalse(names_set_before ^ names_set_after)

    def test_rename_files(self):
        raise NotImplementedError

    def test_rename_dirs(self):
        raise NotImplementedError

    def test_rename_file_if_name_already_exists(self):
        raise NotImplementedError

    def test_rename_dir_if_name_already_exists(self):
        raise NotImplementedError


if __name__ == "__main__":
    unittest.main()
