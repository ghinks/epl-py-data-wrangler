import unittest
from src.parsers.csv.csvDataParser import CSVReader

class TestCSVParser(unittest.TestCase):
    def test_something(self):
        # TODO why the full path only, why not relative
       reader = CSVReader("/home/glenn/dev/epl-predictor/data/eplCSV2000-2018/data.csv")
       results = reader.read()
       self.assertEqual(results.empty, False)


if __name__ == '__main__':
    unittest.main()
