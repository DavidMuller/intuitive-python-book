import unittest
from pathlib import Path


class TestDirectoryLayout(unittest.TestCase):
    def test_tests_layout_matches_j_park(self):
        # verify that this file is - itself - in tests/
        this_files_path = Path(__file__)
        tests_dir = this_files_path.parent
        self.assertEqual(tests_dir.name, "tests")

        # get a path to the j_park/ source directory
        j_park_path = Path(tests_dir.parent, "j_park")

        # loop through all test_*.py files in tests/
        # (and its subdirectories)
        for test_file_path in tests_dir.glob("**/test_*.py"):
            # skip this file: we don't expect there to be a
            # corresponding source file for this layout enforcer
            if test_file_path == this_files_path:
                continue

            # construct the expected source_path
            source_rel_dir = test_file_path.relative_to(tests_dir).parent
            source_name = test_file_path.name.split("test_", maxsplit=1)[1]
            source_path = Path(j_park_path, source_rel_dir, source_name)

            error_msg = (
                f"{test_file_path} found, but {source_path} missing."
            )
            self.assertTrue(source_path.is_file(), msg=error_msg)
