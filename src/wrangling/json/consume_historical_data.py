import pandas as pd
from src.discovery.discover_files_in_folder import DiscoverDataFiles
from src.parsers.json.json_data_parser import JsonReader
import numpy


class ConsumeHistoricalJsonData:
    """Given a path and a glob create a pandas data frame from many JSON files


    The historical data that is used in this project can come in JSON format.
    Take the historical JSON files that exist at the path given and use a glob
    to discover the files that exist. When the files have been discovered the
    data from the JSON files is read into Pandas DataFrames. These frames are
    then concatenated into a single DataFrame
    """
    def __init__(self):
        self.path = "data/historicalData"
        self.glob = "*.json"

    def consume(self):
        discover = DiscoverDataFiles(self.path, self.glob)
        fileNames = discover.read()
        jsonDataSets = []
        for fileName in fileNames:
            parser = JsonReader(fileName)
            data = parser.read()
            jsonDataSets.append(data)
        return jsonDataSets

    def concat(self):
        setsOfData = self.consume()
        conglomoratedData = pd.concat(setsOfData, sort=False)
        return conglomoratedData

    def get_distinct_team_names(self, data):
        distinctTeamNames = data.loc[:, "standardHomeTeamName"].unique()
        return numpy.sort(distinctTeamNames)





