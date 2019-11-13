import pandas as pd
import re

"""class to read in data from json"""
class reader:
    fileName = ''

    def __init__(self, fileName):
        self.fileName = fileName

    def convertTeamName(self, name):
        """convert string to upper case and strip spaces

        Take the given team name remove whitespace and
        convert to uppercase
        """
        upper = name.upper()
        converted = re.sub(r"\s+", "", upper)
        return converted

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
    file = reader("./data/historicalData/season-0910_json.json")
    file.read()
    print(reader.fileName)

if __name__ == "__main__":
    readSingleFile()

