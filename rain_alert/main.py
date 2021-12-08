import requests
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

# Twilio
API_KEY = '**********'
ACCOUNT_SID = '**********'
AUTH_TOKEN = '**********'
TWILIO_NUMBER = '**********'
MY_VOIP_NUMBER = '**********'

LAT = '**********'
LONG = '**********'

weather_params = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'units': 'metric',
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]  # Weather conditions for the next 12 hours

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:  # Weather conditions codes https://openweathermap.org/weather-conditions
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body='It\'s going to rain today. Remember to bring an umbrella.',
        from_=TWILIO_NUMBER,
        to=MY_VOIP_NUMBER
    )

    print(message.sid)
