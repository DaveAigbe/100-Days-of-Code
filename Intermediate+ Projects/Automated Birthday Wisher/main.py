import smtplib
import datetime as dt
from random import choice
import pandas
import os

# Enter your name for personalized email
YOUR_NAME = "Dave"


# Create a dataframe of all the information needed and format each birthday entry into a dictionary
birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")

# Produce current date and format a string to use for matching
current_date = dt.datetime.now()
date_string = f"{current_date.month}/{current_date.day}"
# Produce a list of all the templates that will be worked with
filename = 'letter_templates'
files = []
for i in os.listdir(filename):
    if i.endswith('.txt'):
        files.append(i)

# If the current day and the birthday match, send out a random birthday email with the individuals name
for index, date in enumerate(birthdays):
    current_birthday = f"{birthdays[index]['month']}/{birthdays[index]['day']}"
    if current_birthday == date_string:
        # Produce a random letter from the templates and format it with the birthday individuals name
        with open(f'{filename}/{choice(files)}', 'r') as letter:
            new_letter = letter.read()

            # Replace the name holder with the birthday individuals name and replace sender_name with your name
            formatted_letter = new_letter.replace('[NAME]', birthdays[index]['name']).replace('[SENDER_NAME]', YOUR_NAME)

            # Send out the email with the content as the formatted letter
            MY_EMAIL = "pythonistatester2000@gmail.com"  # <- Enter your own email
            recipient = birthdays[index]['email']

            # Password
            PASSWORD = "daveisepic"  # <- Enter your own password

            with smtplib.SMTP("smtp.gmail.com") as connect:  # <- Enter your own email provider smtp connection EX: smtp.mail.yahoo.com
                connect.starttls()  # <- Secure the connection

                connect.login(user=MY_EMAIL, password=PASSWORD)  # <- Login to your email

                # Send the email with the subject as "HAPPY BIRTHDAY"
                connect.sendmail(from_addr=MY_EMAIL, to_addrs=recipient,  msg=f"Subject:HAPPY BIRTHDAY\n\n{formatted_letter}")
