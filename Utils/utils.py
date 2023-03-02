import sqlparse
from difflib import SequenceMatcher


# THIS FUNCTION WILL CALCULATE SIMILARITY REPORT
def calculateSimilarityReport(query1, query2):
    parsed_query1 = sqlparse.parse(query1)[0]
    parsed_query2 = sqlparse.parse(query2)[0]
    similarity_ratio = SequenceMatcher(None, str(parsed_query1), str(parsed_query2)).ratio()
    return similarity_ratio

query1 = "SELECT * FROM table WHERE id = 1"
query2 = "SELECT id, name FROM table WHERE id = 1"
similarity_ratio = calculateSimilarityReport(query1, query2)
print(f"The similarity ratio between the queries is: {similarity_ratio}")
