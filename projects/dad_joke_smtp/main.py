# Gmail: smtp.gmail.com

import smtplib, os, requests, schedule, time
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DESTINATION = os.environ.get("DESTINATION")

def get_dadjoke():
    headers = {'Accept': 'application/json'}
    api_url = f'https://icanhazdadjoke.com/'
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        # print(response.json())
        joke=response.json()['joke']
        return joke
    else:
        print("Error:", response.status_code, response.text)
        return "No joke."

def send_dadjoke():
    
    joke = get_dadjoke()
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=DESTINATION, 
                            msg=f"Subject: Dad Joke of the minute\n\n{joke}".encode("utf-8"))

if __name__ == "__main__":
    #schedule.every(1).minutes.do(send_dadjoke)
    schedule.every(3).seconds.do(send_dadjoke)
    
    errors: int = 0
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except UnicodeEncodeError as e:
            errors += 1
            print(e)
            print("errors encountered:", errors)