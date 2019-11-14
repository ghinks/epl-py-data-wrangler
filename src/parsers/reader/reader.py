import re

class Reader:
    fileName = ""

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