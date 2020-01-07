import pandas as pd


class HotEncode():
    def __init__(self, data, columns, prefix, separator):
        self.data = data
        self.columns = columns
        self.prefix = prefix
        self.separator = separator

    def create_hot_encoding(self):
        df_processed = pd.get_dummies(data=self.data, prefix_sep=self.separator, prefix=self.prefix,
                                      columns=self.columns)
        return df_processed


def hotEncodeData(data):
    hot_encoder = HotEncode(data, ["standardHomeTeamName", "standardAwayTeamName", "FTR"],
                            ["HOME_TEAM", "AWAY_TEAM", "FTR"],
                            ["_", "_", "_"])
    data = hot_encoder.create_hot_encoding()
    return data
