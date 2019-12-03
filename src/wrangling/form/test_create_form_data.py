import numpy as np
import pandas as pd
import unittest
from src.parsers.csv.csv_data_parser import CSVReader
from src.wrangling.form.create_form_data import CreateFormData
import datetime

class TestCreateFormData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = CSVReader("data/football-data/1819.csv")
        cls.test_data = parser.read()

    def test_partition_by_team(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        partitioned = creator.partition_by_team()
        self.assertGreater(len(partitioned["ARSENAL"]), 0)

    def test_is_win(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        # create a single pandas data frame that contains a winning game
        test_data_frame = pd.DataFrame({
            "standardHomeTeamName": ["ARSENAL"],
            "standardAwayTeamName": ["CHELSEA"],
            "FTR": ["H"]
        })
        result = creator.is_win(test_data_frame.iloc[0], "ARSENAL")
        self.assertTrue(result)

    def test_is_not_win_as_team_is_unknown(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        test_data_frame = pd.DataFrame({
            "standardHomeTeamName": ["ARSENAL"],
            "standardAwayTeamName": ["CHELSEA"],
            "FTR": ["H"]
        })
        result = creator.is_win(test_data_frame.iloc[0], "unknown")
        self.assertFalse(result)

    def test_is_not_win_as_it_is_a_draw(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        test_data_frame = pd.DataFrame({
            "standardHomeTeamName": ["ARSENAL"],
            "standardAwayTeamName": ["CHELSEA"],
            "FTR": ["D"]
        })
        result = creator.is_win(test_data_frame.iloc[0], "ARSENAL")
        self.assertFalse(result)

    def test_is_lose(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        test_data_frame = pd.DataFrame({
            "standardHomeTeamName": ["ARSENAL"],
            "standardAwayTeamName": ["CHELSEA"],
            "FTR": ["H"]
        })
        result = creator.is_lose(test_data_frame.iloc[0], "CHELSEA")
        self.assertTrue(result)

    def test_is_draw(self):
        creator= CreateFormData(TestCreateFormData.test_data)
        test_data_frame = pd.DataFrame({
            "standardHomeTeamName": ["ARSENAL"],
            "standardAwayTeamName": ["CHELSEA"],
            "FTR": ["D"]
        })
        result = creator.is_draw(test_data_frame.iloc[0])
        self.assertTrue(result)

    def test_create_partition_by_team(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        partitioned = creator.partition_by_team()
        arsenal = partitioned["ARSENAL"]
        for key, values in partitioned.items():
            self.assertEqual(len(partitioned[key]), 38)

    def test_create_form_dictionary(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        partitioned = creator.partition_by_team()
        form_dictionary = creator.create_form_dictionary(partitioned)
        self.assertEqual(len(form_dictionary), 20)
        arsenal_form = form_dictionary['ARSENAL']
        self.assertEqual(len(arsenal_form), 38)
        max_form = max(arsenal_form.values())
        self.assertLess(max_form, 16)
        min_form = min(arsenal_form.values())
        self.assertEqual(min_form, 0)
        arsenal_on_2018_12_8 = arsenal_form[datetime.date(2018, 12, 8)]
        self.assertIsNotNone(arsenal_on_2018_12_8)

    def test_update_data_frame_with_form(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        games = creator.update_data_frame_with_form()
        self.assertIsNotNone(games)
        results = np.append(np.where(games["awayTeamForm"] >= 0, True, False), (np.where(games["homeTeamForm"] >= 0, True, False)))
        self.assertTrue(all(results))

if __name__ == '__main__':
    unittest.main()
