import unittest
from src.wrangling.csv.consume_historical_data import ConsumeHistoricalCSVData

class TestConsumeCSVHistoricalData(unittest.TestCase):
    def test_creation(self):
        consumer = ConsumeHistoricalCSVData()
        data = consumer.consume()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)


    def test_concat(self):
        consumer = ConsumeHistoricalCSVData()
        conglomoratedData = consumer.concat()
        self.assertIsNotNone(conglomoratedData)
        print(conglomoratedData.head())
        print(conglomoratedData.tail(5))


    def test_distinct_team_names(self):
        consumer = ConsumeHistoricalCSVData()
        concatedData = consumer.concat()
        distinctNames = consumer.get_distinct_team_names(concatedData)
        self.assertGreater(len(distinctNames), 0)
        print(distinctNames)


if __name__ == '__main__':
    unittest.main()
