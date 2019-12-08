import re
import datetime

class Reader:
    fileName = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def convertTeamName(self, name):
        """convert string to upper case and strip spaces

        Take the given team name remove whitespace and
        convert to uppercase
        """
        try:
            upper = name.upper()
            converted = re.sub(r"\s+", "", upper)
            return converted
        except Exception as e:
            print(f"an exception when trying to convert ${name} to upper case has taken place ${e}")
            raise

    def convertStrDate(self, strDate):
        """given dd/mm/yyyy or yyyy-mm-dd create a python Date

        Take the string format of 'dd/mm/yyyy' or 'yyyyy-mm-dd'
        and convert that into a form that may be used to create
        a python date
        """
        if not isinstance(strDate, str):
            return strDate
        try:
            compiled = re.compile(r"(\d\d)\/(\d\d)\/(\d{2,4})")
            match = compiled.match(strDate)
            if match:
                day = match.groups()[0]
                month = match.groups()[1]
                year = match.groups()[2]
                # there are two types of year format that can be given
                # the first is a 2 digit year. If this year is > 80
                # then it was before year 2000
                # if it is < 80 it is after year 2000
                if len(year) == 2 and 80 < (int(year)) < 100:
                    year = (int(year)) + 1900
                elif len(year) == 2 and (int(year)) < 80:
                    year = 2000 + int(year)
                return datetime.date(int(year), int(month), int(day))
            compiled = re.compile(r"(\d\d\d\d)\-(\d\d)\-(\d\d)(.*)")
            match = compiled.match(strDate)
            year = match.groups()[0]
            month = match.groups()[1]
            day = match.groups()[2]
            return datetime.date(int(year), int(month), int(day))
        except (ValueError, AttributeError, TypeError):
            print("error handling date ", strDate)
            raise
