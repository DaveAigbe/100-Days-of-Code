import smtplib
import datetime as dt
from random import choice

# Produces current date and time
current_time = dt.datetime.now()

# Produce the day of the week in number format 0-6
current_day = current_time.weekday()

# If the day is monday
filename = "quotes.txt"
if current_day == 0:
    with open(filename, 'r') as f:
        quotes = f.read().split("\n")

    # Emails to be used
    MY_EMAIL = "pythonistatester2000@gmail.com"  # <- Enter the email it will be sent from + the recipient
    recipient = "pythonistatester2000@yahoo.com"

    # Password
    PASSWORD = ""  # <- Enter sender password

    # Connect to email providers SMTP server, takes in the server as the argument
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secures connection
        connection.starttls()

        # Login using email name and password
        connection.login(user=MY_EMAIL, password=PASSWORD)

        # Send email
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipient,
                            msg=f"Subject:Monday Motivation\n\n{choice(quotes)}")
