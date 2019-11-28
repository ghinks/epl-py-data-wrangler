import pandas as pd
import unittest
from src.parsers.csv.csv_data_parser import CSVReader
from src.wrangling.form.create_form_data import CreateFormData

class TestCreateFormData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = CSVReader("/home/glenn/dev/epl-predictor/data/football-data/1819.csv")
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

    @unittest.skip("not ready to update with form yet")
    def test_update_data_frame_with_form(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        updated_data = creator.update_data_frame_with_form()
        self.assertGreater(len(updated_data["FORM"]), 0)

if __name__ == '__main__':
    unittest.main()
