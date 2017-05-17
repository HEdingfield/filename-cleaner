import unittest
from pathlib import Path
from fc import filename_cleaner


class Test(unittest.TestCase):
    def setUp(self):
        self.input_path = Path.cwd().__str__() + '\\testing'
        if not Path(self.input_path).exists():
            Path(self.input_path).mkdir(parents=True)
        self.bad_chars = '\/*?:"<>|'
        self.replacement_char = '_'
        self.clean_type = 'both'
        self.actually_rename = False

        # Create temporary files and directories to test on
        Path(self.input_path + "\\test1.txt").touch()
        Path(self.input_path + '\\t1est.t1xt').touch()
        Path(self.input_path + '\\test.txt').touch()
        bad_dir_path = self.input_path + '\\bad1dir'
        Path(bad_dir_path).mkdir(parents=True)
        Path(bad_dir_path + "\\test1.txt").touch()
        Path(bad_dir_path + '\\t1est.t1xt').touch()
        Path(bad_dir_path + '\\test.txt').touch()
        good_dir_path = self.input_path + '\\gooddir'
        Path(good_dir_path).mkdir(parents=True)
        Path(good_dir_path + "\\test1.txt").touch()
        Path(good_dir_path + '\\t1est.t1xt').touch()
        Path(good_dir_path + '\\test.txt').touch()

    def tearDown(self):
        # Delete all temporary files and directories created
        def delete_folder(path):
            for sub in path.iterdir():
                if sub.is_dir():
                    delete_folder(sub)
                else:
                    sub.unlink()
            path.rmdir()

        delete_folder(Path(self.input_path))

    def test_bad_input_dir(self):
        input_path = self.input_path + '\\bad_path\\'
        self.assertRaises(NotADirectoryError, filename_cleaner, input_path, self.bad_chars, self.replacement_char,
                          self.clean_type, self.actually_rename)

    def test_no_rename(self):
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
