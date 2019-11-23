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

    def test_create_form_dictionary(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        partitioned = creator.partition_by_team()
        form_data_by_team = creator.create_form_dictionary(partitioned)
        arsenal = form_data_by_team["ARSENAL"]
        self.assertGreater(len(arsenal), 0)

    def test_update_data_frame_with_form(self):
        creator = CreateFormData(TestCreateFormData.test_data)
        updated_data = creator.update_data_frame_with_form()
        self.assertGreater(len(updated_data["FORM"]), 0)

if __name__ == '__main__':
    unittest.main()
