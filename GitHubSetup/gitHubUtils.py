import datetime
from Configs.config import ORG_NAME
import sqlparse
from difflib import SequenceMatcher
import pandas as pd

def getCurrentSeason():
    # Get the current month of the year
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    # Check if it's fall (September, October, or November)
    if month in [8, 9, 10]:
        return ("FALL", 1, year) 
    
    elif month in [10, 11]:
        return ("FALL", 2, year)
    
    # Check if it's spring (March, April, or May)
    elif month in [1, 2]:
        return ("SPRING", 1, year)
        
    elif month in [3, 4]:
        return ("SPRING", 2, year)

    # Otherwise, it's neither fall nor spring
    else:
        return ("SUMMER", 1, year)


def getOrgName():
    global ORG_NAME
    result = getCurrentSeason()
    ORG_NAME = ORG_NAME.format(result[0], result[2], result[1])
    return ORG_NAME



"""
file1 = "path/to/file1.sql"
file2 = "path/to/file2.sql"

similarity_ratio = compare_sql_files(file1, file2)

print(f"The similarity ratio between {file1} and {file2} is: {similarity_ratio}")
"""
def compare_sql_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        sql1 = f1.read()
        sql2 = f2.read()

    parsed_sql1 = sqlparse.parse(sql1)[0]
    parsed_sql2 = sqlparse.parse(sql2)[0]

    similarity_ratio = SequenceMatcher(None, str(parsed_sql1), str(parsed_sql2)).ratio()

    return similarity_ratio


def readGitHubUserNames(filePath="../Data/data.csv"):
    csv = pd.read_csv(filePath)
    return csv['GitHub_Username']



