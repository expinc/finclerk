import re

# YYYY-MM-DD
datetime_pattern = r"\d\d\d\d-\d\d-\d\d"

def check_date_format(date):
    if not re.match(datetime_pattern, date):
        raise Exception("Invalid date format: {}, expects: YYYY-MM-DD".format(date))
