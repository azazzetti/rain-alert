import requests
from twilio.rest import Client

account_sid = "COMPLETE YOUR OWN ACCOUNT SID"
auth_token = "COMPLETE YOUR OWN AUTH TOKEN"
API_KEY = "COMPLETE YOUR OWN API KEY"
lat = 42.576881
long = 1.667760
parameters={
    "lat": lat,
    "lon": long,
    "appid": API_KEY,
    "cnt": 4,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+19123015125",
        body="Bring an Umbrella",
        to="+376669262"
    )

    print(message.status)
else:
    print("No rain bro")