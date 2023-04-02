##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib, pandas
import datetime as dt
from random import choice

def import_birthdays():
    try:
        birthdays_df = pandas.DataFrame(pandas.read_csv("birthdays.csv"))
    except FileNotFoundError:
        print("Birthdays could not be found. Exiting program.")
        quit()
        
    birthdays = ""
    return birthdays_df

def pick_letter(name):
    letter = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    with open(f"letter_templates/{letter}", "r", encoding="utf-8") as file:
        letter_list = file.readlines()
        letter_list[0] = letter_list[0].replace("[NAME]", name)
        birthday_letter = "".join(letter_list)
    return birthday_letter
    
def send_wishes(birthday_person):
    EMAIL = ""
    PASSWORD = ""
    birthday_name = birthday_person[0]
    destination = birthday_person[1]
    message = pick_letter(birthday_name)
    # print(message)
    
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=destination,
                            msg=f"{message}".encode("utf-8"))
    

def check_birthdays(birthdays):
    celebrators = []
    today = dt.datetime.now()
    for person in birthdays.index:
        if today.month == birthdays["month"][person] and today.day == birthdays["day"][person]:
            celebrators.append((birthdays["name"][person], birthdays["email"][person]))
    
    return celebrators

def main():
    birthdays: pandas.DataFrame = import_birthdays()
    celebrators = check_birthdays(birthdays)
    for person in celebrators:
        send_wishes(person)
    
    
if __name__ == "__main__":
    main()