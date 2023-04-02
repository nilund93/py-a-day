# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
# If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

import smtplib
import datetime as dt
# smtplib.SMTP("smtp.gmail.com", port=587)
MY_EMAIL = ""
PASSWORD = ""
DESTINATION = ""

def smtp_send_msg():
    # this can be done with a context manager
    # aka with-keyword
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=DESTINATION, 
                        msg="This is a message.")
    connection.close()


"""
Create a special password in security settings in your GOOGLE account.
Security tab, 2FA needs to be added.
Add an app-password.
Select "other" app, describe it and add it to the program.
"""

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
date_of_birth = dt.datetime(year=1993, month=12, day=20)
print(date_of_birth)