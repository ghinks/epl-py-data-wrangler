import os
import pandas as pd
from src.discovery.discover_files_in_folder import DiscoverDataFiles
from src.parsers.csv.csv_data_parser import CSVReader
import numpy
import re

class ConsumeHistoricalCSVData:
    """Given a path and a glob create a pandas data frame from many CSV files


    The historical data that is used in this project can come in CSV format.
    Take the historical CSV files that exist at the path given and use a glob
    to discover the files that exist. When the files have been discovered the
    data from the CSV files is read into Pandas DataFrames. These frames are
    then concatenated into a single DataFrame
    """
    def __init__(self):
        self.path = "data/football-data"
        self.glob = "*.csv"

    def cleanTrailingCommas(self, file):
        """Clean multiple trailing empty comma columns

        arguments: fileName(fully qualified)
        uses a temp "cleaned" file name to write to
        returns original file.
        """
        cleanedFile = file.split(".csv")[0] + ".cleaned.csv"
        with open(file, "r") as sourceFile, open(cleanedFile, "w") as destFile:
            lineNum = 1
            try:
                line = sourceFile.readline()
                while line:
                    tc = re.compile("(^.*?)(,{2,}$)")
                    match = tc.match(line)
                    if match:
                        destFile.write(match.group(1) + "\n")
                    else:
                        destFile.write(line)
                    line = sourceFile.readline()
                    lineNum += 1
            except UnicodeDecodeError as e:
                print(f"cleaning error at line {lineNum} {line} {type(e).__name__} {e}")
        os.remove(file)
        os.rename(cleanedFile, file)
        return file

    def consume(self):
        discover = DiscoverDataFiles(self.path, self.glob)
        fileNames = discover.read()
        cleanedFileNames = []
        for fileName in fileNames:
            try:
                cleanedFileNames.append(self.cleanTrailingCommas(fileName))
            except Exception as cleanerError:
                print(f"Error cleaning file {fileName} {cleanerError}")
        csvDataSets = []
        for fileName in cleanedFileNames:
            try:
                parser = CSVReader(fileName)
            except Exception as eReader:
                print(f"Error creating CSV Reader {eReader}")
            try:
                data = parser.read()
                csvDataSets.append(data)
            except Exception as e:
                print(f"Error handling parse {fileName} {e}")
        return csvDataSets

    def concat(self):
        setsOfData = self.consume()
        conglomoratedData = pd.concat(setsOfData, sort=False)
        return conglomoratedData

    def get_distinct_team_names(self, data):
        distinctTeamNames = data.loc[:, "standardHomeTeamName"].unique()
        return numpy.sort(distinctTeamNames)

