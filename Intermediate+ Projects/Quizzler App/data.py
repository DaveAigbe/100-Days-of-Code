import requests
import pprintjson

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

question_data = response.json()
pprintjson.pprintjson(question_data)