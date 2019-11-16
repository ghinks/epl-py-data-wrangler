import unittest
from src.parsers.json.json_data_parser import jsonReader

class testJsonReader(unittest.TestCase):
    def testNameConversion(self):
        json = jsonReader("fake file")
        clubName = json.convertTeamName("Man Utd")
        self.assertEqual("MANUTD", clubName)

    def testJsonReading(self):
        file = jsonReader("/home/glenn/dev/epl-predictor/data/historicalData/season-0910_json.json")
        file.read()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
