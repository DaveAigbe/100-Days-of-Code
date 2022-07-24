import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = 32.826520
MY_LONG = -96.946410

# <-----------------------------------------------------------Produce current position----------------------------------------------------------------------------->

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

# <----------------------------------------------------------------Calculate time------------------------------------------------------------------------>

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

sunrise_hour = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset_hour = int(data["results"]["sunset"].split('T')[1].split(':')[0])

current_hour = datetime.now().hour


# <-------------------------------------------------------Function to check all conditions--------------------------------------------------------------------------------->

# Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5) and (
            current_hour > sunset_hour + 1):
        return True
    else:
        return False


# <-------------------------------------------------------Send out Email--------------------------------------------------------------------------------->
while True:
    sleep(60)  # Runs every minute to check
    if is_overhead():
        MY_EMAIL = "pythonistatester2000@gmail.com"
        recipient = "pythonistatester2000@yahoo.com"

        PASSWORD = "daveisepic"

        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()

            connect.login(user=MY_EMAIL, password=PASSWORD)
            connect.sendmail(from_addr=MY_EMAIL, to_addrs=recipient,
                             msg="Subject: Go outside, look up!\n\nThe ISS is currently overhead look up!")


