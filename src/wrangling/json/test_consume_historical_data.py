import unittest
from src.wrangling.json.consume_historical_data import ConsumeHistoricalJsonData
import pytest
class TestConsumeJsonData(unittest.TestCase):
    @pytest.mark.skip(reason="relative path issues")
    def test_creation(self):
        consumer = ConsumeHistoricalJsonData()
        data = consumer.consume()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    @pytest.mark.skip(reason="relative path issues")
    def test_concat(self):
        consumer = ConsumeHistoricalJsonData()
        conglomoratedData = consumer.concat()
        self.assertIsNotNone(conglomoratedData)
        print(conglomoratedData.head())
        print(conglomoratedData.tail(5))

    @pytest.mark.skip(reason="relative path issues")
    def test_distinct_team_names(self):
        consumer = ConsumeHistoricalJsonData()
        concatedData = consumer.concat()
        distinctNames = consumer.get_distinct_team_names(concatedData)
        self.assertGreater(len(distinctNames), 0)
        print(distinctNames)

if __name__ == '__main__':
    unittest.main()
