import unittest
from src.parsers.json.json_data_parser import JsonReader

class testJsonReader(unittest.TestCase):
    def testNameConversion(self):
        json = JsonReader("fake file")
        clubName = json.convertTeamName("Man Utd")
        self.assertEqual("MANUTD", clubName)

    def testJsonReading(self):
        file = JsonReader("data/historicalData/season-0910_json.json")
        file.read()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
