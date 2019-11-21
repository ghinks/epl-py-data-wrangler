import unittest
from src.wrangling.json.consume_historical_data import ConsumeHistoricalData

class TestConsumeJsonData(unittest.TestCase):
    def test_creation(self):
        consumer = ConsumeHistoricalData()
        data = consumer.consume()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_concat(self):
        consumer = ConsumeHistoricalData()
        conglomoratedData = consumer.concat()
        self.assertIsNotNone(conglomoratedData)
        print(conglomoratedData.head())
        print(conglomoratedData.tail(5))

    def test_distinct_team_names(self):
        consumer = ConsumeHistoricalData()
        concatedData = consumer.concat()
        distinctNames = consumer.get_distinct_team_names(concatedData)
        self.assertGreater(len(distinctNames), 0)
        print(distinctNames)

if __name__ == '__main__':
    unittest.main()
