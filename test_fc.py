import unittest
from pathlib import Path
from fc import filename_cleaner


class Test(unittest.TestCase):
    def setUp(self):
        # Create temporary files and directories to test on
        self.testing_path = Path.cwd().__str__() + "\\testing"
        if not Path(self.testing_path).exists():
            Path(self.testing_path).mkdir(parents=True)

    def tearDown(self):
        # Delete all temporary files and directories created
        p = Path(self.testing_path)
        for f in p.glob('**/*'):
            if f.is_file():
                f.unlink()
        p.rmdir()

    def test_bad_input_dir(self):
        folder = self.testing_path + "\\bad_path\\"
        clean_type = "dirs"
        bad_chars = '\/*?:"<>|'
        replacement_char = "_"
        actually_rename = False
        self.assertRaises(NotADirectoryError, filename_cleaner, folder, clean_type, bad_chars, replacement_char, actually_rename)

    def test_no_rename(self):
        raise NotImplementedError

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
