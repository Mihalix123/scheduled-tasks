import smtplib
from random import choice
import datetime as dt
import os

all_quotes = []
with open("quotes.txt", "r") as file:
    quotes = file.readlines()
for quote in quotes:
    all_quotes.append(quote)

quote_to_send = choice(all_quotes)

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="michu.johnson@yahoo.com", msg=f"Subject: Quote for friday!\n\n {quote_to_send}")
