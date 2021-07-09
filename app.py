from flask import Flask, request, render_template, url_for
import requests
import configparser

app = Flask(__name__)

api_key = "e97d94689fcc0bf2f370a361d61a7382"

def weather_info(city_name, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()


@app.route('/')
def method_name():
   return render_template('home.html')

@app.route('/weather', methods = ['POST', 'GET'])
def weather_app():
    city_name = request.form['cityname']
    data = weather_info(city_name, api_key)
    temp = str(data["main"]["temp"])
    desc = data["weather"][0]["description"]
    desc = desc.capitalize()
    country = data["sys"]["country"]
    return render_template('weather.html', cityname = city_name, temperature = temp, description = desc, country = country)


@app.errorhandler(401)
def page2(e):
    flash("Please enter the city in the following format - New Delhi, London, New York, etc")
    return redirect(url_for('method_name'))
    
@app.errorhandler(400)
def page3(e):
    flash("Please enter the city in the following format - New Delhi, London, New York, etc")
    return redirect(url_for('method_name'))
@app.errorhandler(403)
def page4(e):
    flash("Please enter the city in the following format - New Delhi, London, New York, etc")
    return redirect(url_for('method_name'))
@app.errorhandler(404)
def page5(e):
    flash("Please enter the city in the following format - New Delhi, London, New York, etc")
    return redirect(url_for('method_name'))

if (__name__) == "__main__":
    app.debug = True
    app.run(debug=True)