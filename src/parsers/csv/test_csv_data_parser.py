import sys
import os
from pathlib import Path
import unittest
from src.parsers.csv.csv_data_parser import CSVReader


class TestCSVParser(unittest.TestCase):
    def test_something(self):
        reader = CSVReader("data/football-data/0304.csv")
        results = reader.read()
        self.assertEqual(results.empty, False)


if __name__ == '__main__':
    unittest.main()
