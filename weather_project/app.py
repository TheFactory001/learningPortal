from flask import Flask, render_template, json, request, Response
import requests
import json
app = Flask(__name__)


def get_weather_details(weather_json):
    weather_description = weather_json["weather"][0]["description"]
    city_temp = weather_json["main"]["temp"]
    return weather_description, city_temp


def create_url(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    key_link_text = "appid="
    API_KEY = "a1d832c101f04481e98ece5a0a6cb290"
    city_link_text = "&q="
    full_link = base_url+key_link_text+API_KEY+city_link_text+city
    return full_link


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user_city = request.form['city']
        my_url = create_url(user_city)
        weather_data = requests.get(my_url)
        data_object = weather_data.json()

        weather_desc, city_temp = get_weather_details(data_object)

        return render_template('index.html', weather_desc=weather_desc, city_temp=f"{city_temp} K , {int(city_temp -273.15)} 0C")

    # if request.method == 'POST':
    #     print("Here")
    #     city = request.form['city']
    #     # url = create_url(city)
    #     print(city)
    #     # city_data = request.form
    #     # if city_data:
    #     #     weather_city = city_data['city']
    #     #
    #     # else:
    #     #     url = "nil"

    #     return Response("WE Good")

    #     # return render_template('index.html', weather_data=url)
    else:
        return render_template('index.html')


@app.route("/weather", methods=['GET', 'POST'])
def new_func():
    user_city = request.form['city']
    my_url = create_url(user_city)

    weather_data = requests.get(my_url)
    data_object = weather_data.json()

    weather_result = get_weather_details(data_object)

    return render_template('output.html', weather_result=weather_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
