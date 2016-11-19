import requests

def get_weather():
	url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=770276a0b8516ededbe2d707f2ba6a12"
	weather_req = requests.get(url)
	weather_json =  weather_req.json()

	# print(weather_json)

	description = weather_json['weather'][0]['description']
	# print(description)
	temp_min = weather_json['main']['temp_min']
	# print(temp_min)
	temp_max = weather_json['main']['temp_max']
	# print(temp_max)

	forecast = "Todays show is "
	forecast += description + 'with a high of ' + str(temp_max)
	forecast += ' and low of ' + str(temp_min)

	return forecast
