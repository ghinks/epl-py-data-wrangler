import pandas as pd
from numpy import sort as numpy_sort

class CreateFormData:
    """initialize with Data, and provide mechanism to create form data

    """
    def __init__(self, historical_data):
       self.historical_data = historical_data

    """take the data and break up by team
    
    
    The data will of course contain all match results but we need to 
    create a dictionary of games by teams by date
    """
    def partition_by_team(self):
        # get the unique teams in this current data frame
        teams = self.historical_data["standardHomeTeamName"].unique()
        teams = numpy_sort(teams)
        games_by_team = {team: [] for team in teams}
        # for each team setup an empty collection
        for team in teams:
            by_home_team = self.historical_data[self.historical_data["standardHomeTeamName"].isin([team])]
            by_away_team = self.historical_data[self.historical_data["standardAwayTeamName"].isin([team])]
            by_team = pd.concat([by_home_team, by_away_team])
            games_by_team[team] = by_team
        return games_by_team

    def create_form_dictionary(self, games_by_team):
        for team, games in games_by_team.items():
            print(team)
            sorted_by_team_by_date = games.sort_values("Date", ascending=False)
            print(sorted_by_team_by_date.head(40))

