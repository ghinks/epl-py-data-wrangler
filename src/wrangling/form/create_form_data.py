import functools
import operator
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
        """create form data

        sort the data and apply form calculations
        """
        WINDOW_LENGTH = 5
        WIN_POINTS= 3.0
        DRAW_POINTS = 1.0
        LOOSE_POINTS = 0.0
        for team, games in games_by_team.items():
            sorted_by_team_by_date = games.sort_values("datestamp", ascending=True)
            print(sorted_by_team_by_date.head())
            item = 0
            window = []
            for i, game in sorted_by_team_by_date.iterrows():
                if len(window) == WINDOW_LENGTH:
                    window.pop(0)
                if self.is_win(game, team):
                    window.append(WIN_POINTS)
                elif self.is_lose(game, team):
                    window.append(LOOSE_POINTS)
                else:
                    window.append(DRAW_POINTS)
                form_value = functools.reduce(operator.add, window)
                # print(f"{team} game {item} form is {form_value} last game result {game['FTR']} home {game['standardHomeTeamName']} away {game['standardAwayTeamName']}")
                item += 1

    def is_win(self, game, team):
        if game["standardHomeTeamName"] == team and game["FTR"] == "H":
            return True
        if game["standardAwayTeamName"] == team and game["FTR"] == "A":
            return True
        return False

    def is_draw(self, game):
        if game["FTR"] == "D":
            return True
        return False

    def is_lose(self, game, team):
        if game["standardHomeTeamName"] == team and game["FTR"] == "A":
            return True
        if game["standardAwayTeamName"] == team and game["FTR"] == "H":
            return True
        return False

    def form_calculator(self, sorted_by_team_by_date, team, window_size):
        """updates the form data

        taking the win/draw/lose and assigning the following value to the sliding window n
        win 3 pts
        draw 1 pt
        lose 0 pt
        The maximum value can be n * 3, the minimum 0
        """

