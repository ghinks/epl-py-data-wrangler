import unittest
from src.parsers import jsonDataParser


class MyTestCase(unittest.TestCase):
    def test_something(self):
        json = jsonDataParser.reader("fake file")
        clubName = json.convertTeamName("Man Utd")
        self.assertEqual("MANUTD", clubName)


if __name__ == '__main__':
    unittest.main()
