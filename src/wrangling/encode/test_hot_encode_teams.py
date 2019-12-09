import unittest
import pandas as pd
from src.wrangling.encode.hot_encode_teams import HotEncodeTeams

class TestHotEncoding(unittest.TestCase):
    def test_one_hot_encoding(self):
        df = pd.DataFrame([["ARSENAL", 20],
                           ["QPR", 10]],
                          columns=["TEAM", "RANK"])
        columns = ["TEAM"]
        prefix = ["TEAM"]
        separator = "_"
        hotEncoder = HotEncodeTeams(df, columns, prefix, separator)
        processed = hotEncoder.create_hot_encoding()
        all_columns = processed.columns.values.tolist()
        self.assertListEqual(["RANK", "TEAM_ARSENAL", "TEAM_QPR"], all_columns)


if __name__ == '__main__':
    unittest.main()
