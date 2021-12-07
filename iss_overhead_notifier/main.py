import requests
from datetime import datetime
import smtplib
import time

# Change these variables below
MY_EMAIL = 'email@gmail.com'
MY_PASSWORD = '123456'
MY_LAT = '-8.052240'
MY_LONG = '-34.928612'
LOCAL_UTC_OFFSET = 3  # Difference between UTC and your timezone


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# We need to know the sunset and the sunrise times to know if the sky is actually dark enough to be able to spot the ISS
def is_nightime():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0]) - LOCAL_UTC_OFFSET
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0]) - LOCAL_UTC_OFFSET

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_nightime():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject: Look at the sky!\n\nThe ISS is above you.'
        )
