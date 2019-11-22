import pandas as pd
from src.parsers.reader.reader import Reader

"""class to read in data from a csv"""
class CSVReader(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

    def read(self):
        """read the csv data from the file


        Read the data from file and convert the team names
        """
        try:
            rawData = pd.read_csv(self.fileName)
            rawData["standardHomeTeamName"] = rawData["HomeTeam"].apply(self.convertTeamName)
            rawData["standardAwayTeamName"] = rawData["AwayTeam"].apply(self.convertTeamName)
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

