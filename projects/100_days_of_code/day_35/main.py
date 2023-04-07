import requests

API_KEY = "ba07515b78764138842cbf65f68b8c63"
MY_LAT = 59.241267
MY_LONG = 18.097766

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current, minutely, daily"
}
address = f"https://api.openweathermap.org/data/3.0/onecall"
response = requests.get(address, params=params)
response.raise_for_status()
data = response.json()
print(data)
weather_slice = data["hourly"][:12] # 12 - 1 gives us up to hour 11

will_rain = False 
for hour_data in weather_slice:
    condition_code = print(hour_data["weather"][0]["id"])
    if int(condition_code) < 700: will_rain = True
    
if will_rain:
    print("bring umbrella")
print(data["hourly"][0]["weather"][0]["id"])