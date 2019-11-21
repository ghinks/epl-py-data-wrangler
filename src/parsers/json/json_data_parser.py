import pandas as pd
from src.parsers.reader.reader import Reader
import re

"""class to read in data from json"""
class JsonReader(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

    def read(self):
        """read the data from file and wrangle it

        Read the data from the json file and apply the conversions
        to the data to get the required data sets
        """
        try:
            rawData = pd.read_json(self.fileName, "records")
            rawData["standardHomeTeamName"] = rawData["HomeTeam"].apply(self.convertTeamName)
            rawData["standardAwayTeamName"] = rawData["AwayTeam"].apply(self.convertTeamName)
            #rawData["standardDate"] = rawData["Date"].apply(self.convertStrDate)
            # selectedData = rawData.loc[:, "standardHomeTeamName"].unique()
            # print(selectedData)
            requiredColumns = [
                "standardHomeTeamName",
                "standardAwayTeamName",
                "FTR",
                "Date"
            ]
            selectedData = rawData.loc[:, requiredColumns]
            return selectedData
        except (KeyError):
            print("error in file ", self.fileName)
            raise

def readSingleFile():
    file = JsonReader("/home/glenn/dev/epl-predictor/data/historicalData/season-0910_json.json")
    file.read()
    print(JsonReader.fileName)

if __name__ == "__main__":
    readSingleFile()

