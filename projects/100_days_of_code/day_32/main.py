import smtplib
import datetime as dt

MY_EMAIL = ""
PASSWORD = ""
DESTINATION = ""

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=DESTINATION, 
                            msg="This is a message.")



"""
Create a special password in security settings in your GOOGLE account.
Security tab, 2FA needs to be added.
Add an app-password.
Select "other" app, describe it and add it to the program.
"""