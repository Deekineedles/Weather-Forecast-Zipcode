import requests
key = "a0baaa9c093f0bcc58fa5a6b946efd25"
zip_code = input("Please enter your 5 digit zip code.")
response = requests.get(url=f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={key}")
response.raise_for_status()
data = response.json()
lat = data["lat"]
lng = data["lon"]


response1 = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={key}&units=imperial")
response1.raise_for_status()
data1 = response1.json()
temperature = round(data1['main']['temp'])
feels_like = round(data1['main']['feels_like'])
description = data1['weather'][0]["description"]
print(f"The forecast in {data1['name']} is currently a {description} with a temperature of {temperature}f"
      f" and a wind chill of {feels_like}f.")
