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
        we require that a dictionary of dictionaries
        shall be created. The first dictionary key will
        be the team name. The value will be another dictionary
        that will contain a dictionary of datestamp to form
        """
        WINDOW_LENGTH = 5
        WIN_POINTS= 3.0
        DRAW_POINTS = 1.0
        LOOSE_POINTS = 0.0
        form_by_team_and_date = {}
        for team, games in games_by_team.items():
            sorted_by_team_by_date = games.sort_values("datestamp", ascending=True)
            item = 0
            window = []
            team_form = {}
            form_by_team_and_date[team] = team_form
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
                item += 1
                team_form[game['datestamp']] = form_value
        return form_by_team_and_date

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

    def update_data_frame_with_form(self):
        """update the given data frame with the form data

        Given the form data add a new column called **form** and
        set the form values to that from the form dictionary
        """
        games_by_team = self.partition_by_team()
        form_by_team = self.create_form_dictionary(games_by_team)

        def convert_form(game, args):
            team_name_for_game = game[args]
            team_form = form_by_team[team_name_for_game]
            game_date = game["datestamp"]
            form_for_game_on_date = team_form[game_date]
            return form_for_game_on_date

        self.historical_data["homeTeamForm"] = self.historical_data.apply(convert_form, axis=1, args=["standardHomeTeamName"])
        self.historical_data["awayTeamForm"] = self.historical_data.apply(convert_form, axis=1, args=["standardAwayTeamName"])
        return self.historical_data

