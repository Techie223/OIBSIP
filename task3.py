import requests

#api key from open weather map api
api_key="e55dbc9b3b5efcd669c485be82c9371e"
city=input("Enter the city : ")

#fetching the details from weather api
current_weather=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")


#fetching the weather details
temp=current_weather.json()['main']['temp']
weath=current_weather.json()['weather'][0]['main']
desc=current_weather.json()['weather'][0]['description']
humid=current_weather.json()['main']['humidity']
wind_speed=current_weather.json()['wind']['speed']

#printing the weather details
print(f'Current weather details of {city}:')
print(f'Temperature is :{temp}')
print(f'Weather is {weath}')
print(f'Description : {desc}')
print(f'Humidity is {humid} grams per cubic metres')
print(f'Wind speed id {wind_speed}')
