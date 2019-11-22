import pandas as pd
import pandas as pd
from src.discovery.discover_files_in_folder import DiscoverDataFiles
from src.parsers.json.json_data_parser import JsonReader
import numpy


class ConsumeHistoricalCSVData:
    """Given a path and a glob create a pandas data frame from many CSV files


    The historical data that is used in this project can come in CSV format.
    Take the historical CSV files that exist at the path given and use a glob
    to discover the files that exist. When the files have been discovered the
    data from the CSV files is read into Pandas DataFrames. These frames are
    then concatenated into a single DataFrame
    """
    def __init__(self):
        self.path = "/home/glenn/dev/epl-predictor/data/football-data"
        self.glob = "*.csv"

    def consume(self):
        discover = DiscoverDataFiles(self.path, self.glob)
        fileNames = discover.read()
        csvDataSets = []
        for fileName in fileNames:
            parser = JsonReader(fileName)
            data = parser.read()
            nsonDataSets.append(data)
        return csvDataSets

    def concat(self):
        setsOfData = self.consume()
        conglomoratedData = pd.concat(setsOfData, sort=False)
        return conglomoratedData

    def get_distinct_team_names(self, data):
        distinctTeamNames = data.loc[:, "standardHomeTeamName"].unique()
        return numpy.sort(distinctTeamNames)




from src.discovery.discover_files_in_folder import DiscoverDataFiles
from src.parsers.json.json_data_parser import JsonReader
import numpy


class ConsumeHistoricalCSVData:
    """Given a path and a glob create a pandas data frame from many JSON files


    The historical data that is used in this project can come in JSON format.
    Take the historical JSON files that exist at the path given and use a glob
    to discover the files that exist. When the files have been discovered the
    data from the JSON files is read into Pandas DataFrames. These frames are
    then concatenated into a single DataFrame
    """
    def __init__(self):
        self.path = "/home/glenn/dev/epl-predictor/data/historicalData"
        self.glob = "*.json"

    def consume(self):
        discover = DiscoverDataFiles(self.path, self.glob)
        fileNames = discover.read()
        csvDataSets = []
        for fileName in fileNames:
            parser = JsonReader(fileName)
            data = parser.read()
            csvDataSets.append(data)
        return csvDataSets

    def concat(self):
        setsOfData = self.consume()
        conglomoratedData = pd.concat(setsOfData, sort=False)
        return conglomoratedData

    def get_distinct_team_names(self, data):
        distinctTeamNames = data.loc[:, "standardHomeTeamName"].unique()
        return numpy.sort(distinctTeamNames)




