import requests

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_parametres = {
    "lat": "41.2995",
    "lon": "69.2401",
    "appid": "",
    "exclude": "current,minutely,daily"
}


responce_code = requests.get(OWM_Endpoint, params=weather_parametres)
responce_code.raise_for_status()
weather_data = responce_code.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
more_info = []
clock_list = []
count = 7

for hourly_data in weather_slice:
    if hourly_data["weather"][0]["id"] < 700:
        will_rain = True
        more_info.append(hourly_data["weather"][0]["description"])
        clock_list.append(count)
    count += 1

if will_rain:
    message = "Today will be:"
    for i in range(len(more_info)):
        message += f"/n{more_info[i]} at {clock_list[i]}"

    url = "https://textbelt.com/text"
    data = {
        'phone': "",
        'message': message,
        'key': 'textbelt'
    }
    response = requests.post(url, data=data)
    status = response.status_code
