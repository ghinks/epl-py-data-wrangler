import unittest
from src.parsers.reader import reader

class testReader(unittest.TestCase):
    def testReaderConverter(self):
        json = reader.Reader("fake file")
        clubName = json.convertTeamName("Man Utd")
        self.assertEqual("MANUTD", clubName)

if __name__ == '__main__':
    unittest.main()
