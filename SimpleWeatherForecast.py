import requests
import json
from tkinter import *

#API Key for OpenWeatherMap, You need to generate your own API Key. You can do this by registering on their website and going to the My API keys tab.
api_key = ""

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["name"], data["weather"][0]["description"], data["main"]["temp"]

def checkIfYouNeedHat(temp):
    if temp <= 0:
        return "Don't even try to go out without a hat!"
    if temp > 0 and temp <= 10:
        return "I think you should wear a hat"
    else:
        return "You should be fine without hat :)"

def display_weather():
    city = city_entry.get()
    name, description, temp = get_weather(city)
    output.config(text=f"{name}: {description}, Temperature right now: {temp}°C ({checkIfYouNeedHat(temp)})")

App_window = Tk()
App_window.title("Simple Weather App")
App_window.configure(bg="#859BFA")

city_label = Label(App_window, text="Enter city name: ")
city_entry = Entry(App_window,width=50,fg="black", bg="#ADCFFF")
submit_button = Button(App_window, text="Get weather information in this city!", command=display_weather)

output = Label(App_window, text="",bg="#859BFA")

city_label.pack()
city_entry.pack()
submit_button.pack()

output.pack()

App_window.mainloop()