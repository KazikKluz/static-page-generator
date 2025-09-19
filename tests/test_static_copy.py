import unittest
import os
import shutil

from pyfakefs.fake_filesystem_unittest import TestCase
from src.main import copy_static


class TestCopyStatic(TestCase):
    """ Contains set ot tests for copy_static function"""

    def setUp(self):
        """Pyfakefs test init function"""
        self.setUpPyfakefs()

    def test_copy_single_file(self):
        """will test copying a sigle file"""

        self.fs.create_file("/static/file1.txt")
        os.makedirs("/public", exist_ok=True)

        copy_static("/static", "/public")

        self.assertTrue(os.path.exists("/public/file1.txt"))

    def test_copy_directory_with_files(self):
        """Will test copying non empty directories"""
        self.fs.create_file("/static/dir1/file1.txt")
        self.fs.create_file("/static/dir1/file2.txt")

        os.makedirs("/public")
        copy_static("/static", "/public")

        self.assertTrue(os.path.exists("/public/dir1/file1.txt"))
        self.assertTrue(os.path.exists("/public/dir1/file2.txt"))

    def text_copy_nested_directories(self):
        """Will test copying nested directories"""
        self.fs.create_file("/static/dir1/subdir1/file1.txt")
        self.fs.create_file("/static/dir1/file2.txt")
        os.makedirs("/public")

        copy_static("/static", "/public")

        self.assertTrue(os.path.exists("/public/dir1/subdir1/file1.txt"))
        self.assertTrue(os.path.exists("/public/dir1/file2.txt"))

    def test_copy_empty_directory(self):
        """Will text copying nested directory"""
        os.makedirs("/static/empty_dir")
        os.makedirs("/public")

        copy_static("/static", "/public")

        self.assertTrue(os.path.isdir("/public/empty_dir"))
        self.assertEqual(os.listdir("/public/empty_dir"), [])

    def test_non_existent_source(self):
        """Wiil test an attempt of copying nonexitent directory"""
        os.makedirs("/public")

        with self.assertRaises(FileNotFoundError):
            copy_static("/nonexistent", "/public")


if __name__ == "__main__":
    unittest.main()
