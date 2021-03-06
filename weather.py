import json, requests
from datetime import datetime
import os
import pytz
import requests
import math

api_key = "INSERT_API_KEY_HERE"
api_url = ("http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}")

def query_api(city):
    try:
        print(api_url.format(city, api_key))
        data = requests.get(api_url.format(city,api_key)).json()
    except Exception as ex:
        print(ex)
        data = None
    return data

