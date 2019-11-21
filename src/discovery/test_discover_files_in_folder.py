import unittest
from src.discovery.discover_files_in_folder import DiscoverDataFiles
import os

class TestDiscovery(unittest.TestCase):
    def test_creation(self):
        folder = "some/folder"
        glob = "*.json"
        discoverer = DiscoverDataFiles(folder, glob)
        self.assertEqual(discoverer.targetFolder, folder)

    def test_read(self):
        discoverer = DiscoverDataFiles(os.getcwd(), "**/*.py")
        files = discoverer.read()
        self.assertGreater(len(files), 0)

if __name__ == '__main__':
    unittest.main()
