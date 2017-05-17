import unittest
from pathlib import Path
from fc import filename_cleaner


class Test(unittest.TestCase):
    def setUp(self):
        self.input_path = Path.cwd().__str__() + '\\testing'
        if not Path(self.input_path).exists():
            Path(self.input_path).mkdir(parents=True)
        self.bad_chars = '!1'
        self.replacement_char = '_'
        self.clean_type = 'both'
        self.actually_rename = False

        # Create temporary files and directories to test on
        Path(self.input_path + "\\test1.txt").touch()
        Path(self.input_path + '\\t!est.t1xt').touch()
        Path(self.input_path + '\\test.txt').touch()
        bad_dir_path = self.input_path + '\\bad1dir'
        Path(bad_dir_path).mkdir(parents=True)
        Path(bad_dir_path + "\\test!.txt").touch()
        Path(bad_dir_path + '\\t1est.t1xt').touch()
        Path(bad_dir_path + '\\test.txt').touch()
        good_dir_path = self.input_path + '\\gooddir'
        Path(good_dir_path).mkdir(parents=True)
        Path(good_dir_path + "\\test1.txt").touch()
        Path(good_dir_path + '\\t1est.t!xt').touch()
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
        names_set_before = set([str(name) for name in Path(self.input_path).glob('**/*')])
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set_after = set([str(name) for name in Path(self.input_path).glob('**/*')])
        self.assertFalse(names_set_before ^ names_set_after)

    def test_rename_files(self):
        self.bad_chars = '!'
        self.clean_type = 'files'
        self.actually_rename = True
        names_set_before = set([str(name) for name in Path(self.input_path).glob('**/*')])
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set_after = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_set_after_reverted = set()
        for name in names_set_after:
            if '.' in name:
                # FIXME: Problem here if working directory contains an underscore
                names_set_after_reverted.add(name.replace('_', '!'))
            else:
                names_set_after_reverted.add(name)
        self.assertFalse(names_set_before ^ names_set_after_reverted)

    def test_rename_dirs(self):
        self.bad_chars = '1'
        self.clean_type = 'dirs'
        self.actually_rename = True
        names_set_before = set([str(name) for name in Path(self.input_path).glob('**/*')])
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set_after = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_set_after_reverted = set()
        for name in names_set_after:
            if '.' in name:
                # FIXME: Problem here and in next clause if working directory contains an underscore
                names_set_after_reverted.add(name.rsplit("\\", 1)[0].replace('_', '1') + "\\" + name.split("\\")[-1])
            else:
                names_set_after_reverted.add(name.replace('_', '1'))
        self.assertFalse(names_set_before ^ names_set_after_reverted)

    def test_rename_both(self):
        self.bad_chars = '!'
        self.actually_rename = True
        names_set_before = set([str(name) for name in Path(self.input_path).glob('**/*')])
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set_after = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_set_after_reverted = set()
        for name in names_set_after:
            # FIXME: Problem here if working directory contains an underscore
            names_set_after_reverted.add(name.replace('_', '!'))
        self.assertFalse(names_set_before ^ names_set_after_reverted)

    def test_fix_all_bad_chars(self):
        self.bad_chars = '!1'
        self.actually_rename = True
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_with_bad_chars_set = set()
        for name in names_set:
            for c in self.bad_chars:
                if c in name:
                    names_with_bad_chars_set.add(name)
        self.assertFalse(names_with_bad_chars_set)

    def test_rename_file_if_name_already_exists(self):
        Path(self.input_path + "\\test!.txt").touch()
        self.bad_chars = '!1'
        self.actually_rename = True
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_with_bad_chars_set = set()
        for name in names_set:
            for c in self.bad_chars:
                if c in name:
                    names_with_bad_chars_set.add(name)
        self.assertEqual(len(names_with_bad_chars_set), 1)

    def test_rename_dir_if_name_already_exists(self):
        bad_dir_path = self.input_path + '\\bad!dir'
        Path(bad_dir_path).mkdir(parents=True)
        self.bad_chars = '!1'
        self.actually_rename = True
        filename_cleaner(self.input_path, self.bad_chars, self.replacement_char, self.clean_type, self.actually_rename)
        names_set = set([str(name) for name in Path(self.input_path).glob('**/*')])
        names_with_bad_chars_set = set()
        for name in names_set:
            for c in self.bad_chars:
                if c in name:
                    names_with_bad_chars_set.add(name)
        self.assertEqual(len(names_with_bad_chars_set), 4)


if __name__ == "__main__":
    unittest.main()
