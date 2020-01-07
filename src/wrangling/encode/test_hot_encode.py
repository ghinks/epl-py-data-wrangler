import unittest
import pandas as pd
from src.wrangling.encode.hot_encode import HotEncode

class TestHotEncoding(unittest.TestCase):
    def test_one_hot_encoding_teams(self):
        df = pd.DataFrame([["ARSENAL", 20],
                           ["QPR", 10]],
                          columns=["TEAM", "RANK"])
        columns = ["TEAM"]
        prefix = ["TEAM"]
        separator = "_"
        hotEncoder = HotEncode(df, columns, prefix, separator)
        processed = hotEncoder.create_hot_encoding()
        all_columns = processed.columns.values.tolist()
        self.assertListEqual(["RANK", "TEAM_ARSENAL", "TEAM_QPR"], all_columns)

    def test_one_hot_encoding_match_result(self):
        df = pd.DataFrame([
            ["A", "ARSENAL"],
            ["H", "WOLVES"],
            ["D", "CHELSEA"]],
            columns=["FTR", "TEAM"])
        columns = ["FTR"]
        prefix = "FTR"
        separator = "_"
        hotEncoder = HotEncode(df, columns, prefix, separator)
        processed = hotEncoder.create_hot_encoding()
        all_columns = processed.columns.values.tolist()
        self.assertListEqual((["TEAM", "FTR_A", "FTR_D", "FTR_H"]), all_columns)

if __name__ == '__main__':
    unittest.main()
