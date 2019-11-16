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
        rawData = pd.read_csv(self.fileName)
        print(rawData)
        return rawData

def readSingleFile():
    file = CSVReader("data/eplCSV2000-2018/data.csv")
    file.read()

if __name__ == "__main__":
    readSingleFile()

