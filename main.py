import requests
from datetime import datetime
import smtplib
import time

my_email = "EMAIL"
password = "PASSWORD"
MY_LONG = -99.901810 # Your longitude
MY_LAT = 43.969517 # Your latitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude = float(data['iss_position']['longitude'])
iss_latitude = float(data['iss_position']['latitude'])

# MY_LONG = iss_longitude # Your longitude
# MY_LAT = iss_latitude# Your latitude
#Your poition is within +5 or -5 degrees of the ISS position
#print(iss_longitude)
#print(iss_latitude)

parameters = {

    "lng": MY_LONG,
    "lat": MY_LAT,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
#print(f"Sunrise {sunrise}")
time_now = int(str(datetime.now()).split(" ")[1].split(":")[0])
#print(f"Sunset {sunset}")
#print(f"Time Now {time_now}")

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if iss_longitude <= (MY_LONG + 5) or iss_longitude <= (MY_LONG - 5):
        if iss_latitude <= MY_LAT + 5 or iss_latitude >= MY_LAT -5:
    # and it's currently dark
            if time_now >= sunset or time_now <= sunrise:
                # Then send me an eamil to tell me to look up
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs="crobt98@yahoo.com",
                                        msg=f"Subject: ISS Satalite over head \n\n Look up")
            else:
                print("nope")

# Bonus: run the code every 60 seconds.
