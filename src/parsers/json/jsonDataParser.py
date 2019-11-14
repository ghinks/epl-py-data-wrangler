import pandas as pd
from src.parsers.reader.reader import Reader
import re

"""class to read in data from json"""
class jsonReader(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

    def read(self):
        """read the data from file and wrangle it

        Read the data from the json file and apply the conversions
        to the data to get the required data sets
        """
        rawData = pd.read_json(self.fileName, "records")
        rawData["standardHomeTeamName"] = rawData["HomeTeam"].apply(self.convertTeamName)
        rawData["standardAwayTeamName"] = rawData["AwayTeam"].apply(self.convertTeamName)
        selectedData = rawData.loc[:, "standardHomeTeamName"].unique()
        print(selectedData)

def readSingleFile():
    file = jsonReader("/home/glenn/dev/epl-predictor/data/historicalData/season-0910_json.json")
    file.read()
    print(jsonReader.fileName)

if __name__ == "__main__":
    readSingleFile()

