import smtplib
import datetime as dt
from random import choice

MY_EMAIL = ""
PASSWORD = ""
DESTINATION = ""

def import_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()
    return quotes

def send_email(quotes: list()):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        message = choice(quotes)
        print(message)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=DESTINATION, 
                            msg=f"Subject: Inspiration of the day\n\n{message}".encode("utf-8"))



def main():
    today = dt.datetime.now()
    day_of_week = today.weekday()
    quotes = import_quotes()
    if day_of_week == 6:
        send_email(quotes)

if __name__ == "__main__":
    main()