import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def setUp(self):
        # Create temporary files and directories to test on
        self.testing_path = Path.cwd().__str__() + "\\testing"
        if not Path(self.testing_path).exists():
            Path(self.testing_path).mkdir(parents=True)
        Path(self.testing_path + '\\test1.txt').touch()

    def tearDown(self):
        # Delete all temporary files and directories created
        p = Path(self.testing_path)
        for f in p.glob('**/*'):
            if f.is_file():
                f.unlink()
        p.rmdir()

    def test_bad_input(self):
        raise NotImplementedError

    def test_no_rename(self):
        raise NotImplementedError

    def test_rename(self):
        raise NotImplementedError

    def test_rename_if_file_already_exists(self):
        raise NotImplementedError


if __name__ == "__main__":
    unittest.main()
