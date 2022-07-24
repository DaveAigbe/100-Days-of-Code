import requests
import pprintjson

# Store the URL for the API call
URL = "http://api.open-notify.org/iss-now.json"

# Make a request to the API and look for any status errors
response = requests.get(url=URL)
response.raise_for_status()

# Store API data in a variable and display it
data = response.json()
pprintjson.pprintjson(data)

print("\n")

# Extract information that is needed
iss_position = (data["iss_position"]["longitude"], (data["iss_position"]["latitude"]))
print(iss_position)