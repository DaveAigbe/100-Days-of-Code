import requests
import pprintjson
import datetime as dt

# API requires longitude and latitude
URL = "https://api.sunrise-sunset.org/json"
MY_LAT = 32.826520
MY_LONG = -96.946410

# Store parameters of API's in dictionary
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted": 0
}

# Use the params argument to pass through all the parameters that will be used to form a proper API call
response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
# pprintjson.pprintjson(data)


sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

current_time = dt.datetime.now().hour

print(f"Current Time: {current_time}")
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")
