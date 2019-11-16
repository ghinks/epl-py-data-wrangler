import sys
import os
from pathlib import Path
import unittest
from src.parsers.csv.csv_data_parser import CSVReader


class TestCSVParser(unittest.TestCase):
    def test_something(self):
        # TODO why the full path only, why not relative
        print(Path(__file__))
        print(os.path.dirname(os.path.abspath(__file__)))
        print(os.path.dirname(sys.modules['__main__'].__file__))
        print(os.path.abspath(os.curdir))
        reader = CSVReader("/home/glenn/dev/epl-predictor/data/eplCSV2000-2018/data.csv")
        results = reader.read()
        self.assertEqual(results.empty, False)


if __name__ == '__main__':
    unittest.main()
