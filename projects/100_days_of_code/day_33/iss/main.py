import requests, smtplib, schedule, time, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Response codes
# 1XX: Hold On
# 2xx: Here you go
# 3xx: Go Away
# 4xx: You screwed up
# 5xx: I screwed up

# 54 to 64
MY_LAT = 59.241267 # Your latitude
MY_LONG = 18.097766 # Your longitude
MY_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
DESTINATION = ""


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_iss_overhead() -> bool:
    """Checks if the ISS is currently close to the location of the user.
        Uses an API to fetch the ISS location.
        
    Returns:
        bool: Tells the user if the ISS is above or not.
    """
     
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

def is_night() -> bool:
    """Uses an API to determine when sunrise and sunset is at the user's location, 
        and calculates if it's dark outside or not.
    

    Returns:
        bool: Returns if it's currently dark.
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    return time_now >= sunset or time_now <= sunrise
        
def send_email() -> None:
    """Gets called if it's dark and ISS is above.
        Sends an email to the given DESTINATION-constant,
        using the constants MY_EMAIL and PASSWORD as credentials.
    """
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=DESTINATION, 
                            msg=f"Subject: The ISS is currently above you.\n\nLook to the skies! The ISS is currently above you and should be visible.".encode("utf-8"))

def check_iss() -> None:
    if is_iss_overhead() and is_night(): send_email()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if __name__ == "__main__":
    schedule.every(1).minutes.do(check_iss)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
