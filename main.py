from src.wrangling.csv.consume_historical_data import ConsumeHistoricalCSVData
from src.wrangling.form.create_form_data import CreateFormData
import pandas
import os
from src.wrangling.encode.hot_encode import hotEncodeData

pandas.set_option("display.max_columns", 10)
consumer = ConsumeHistoricalCSVData()
data = consumer.consume()
formDataAdder = CreateFormData(pandas.concat(data))
games = formDataAdder.update_data_frame_with_form()
games = hotEncodeData(games)
print(games[0:3])
print(f"total number of games is {len(games)}")
fileName = "data/feature-engineered-football-data/data.csv"
if os.path.exists(fileName):
    os.remove(fileName)
# columns = ["standardHomeTeamName", "standardAwayTeamName", "FTR", "datestamp", "homeTeamForm", "awayTeamForm"]
games = games.sort_values(["datestamp"])
games.to_csv(fileName, index=False)
