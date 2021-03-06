import unittest
from src.parsers.reader import reader
import datetime

class testReader(unittest.TestCase):
    def testReaderConverter(self):
        json = reader.Reader("fake file")
        clubName = json.convertTeamName("Man Utd")
        self.assertEqual("MANUTD", clubName)

    def test_date_conversion_form_one(self):
        baseReader = reader.Reader("")
        test_date = "13/12/2000"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(2000, 12, 13), pyDate)

    def test_date_conversion_form_two(self):
        baseReader = reader.Reader("")
        test_date = "2000-12-13"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(2000, 12, 13), pyDate)

    def test_date_conversion_form_two(self):
        baseReader = reader.Reader("")
        test_date = "15/08/00"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(2000, 8, 15), pyDate)

    def test_date_conversion_form_two(self):
        baseReader = reader.Reader("")
        test_date = "15/08/98"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(1998, 8, 15), pyDate)

    def test_date_conversion_ddmmyyyy(self):
        baseReader = reader.Reader("")
        test_date = "21/04/2003"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(2003, 4, 21), pyDate)

    def test_date_conversion_ddmmyy(self):
        baseReader = reader.Reader("")
        test_date = "11/05/02"
        pyDate = baseReader.convertStrDate(test_date)
        self.assertIsNotNone(pyDate)
        self.assertEqual(datetime.date(2002, 5, 11), pyDate)

    def test_date_conversion_form_bad_format(self):
        baseReader = reader.Reader("")
        test_date = "xxxxxx"
        # pyDate = baseReader.convertStrDate(test_date)
        self.assertRaises(AttributeError, baseReader.convertStrDate, test_date)


if __name__ == '__main__':
    unittest.main()
