from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):
    
    latitude_range = (-90, 90)
    longitude_range = (-180, 180)
    
    def __init__(self, latitude, longitude):
        super().__init__(location = [latitude, longitude])
        
        self.latitude = latitude
        self.longitude = longitude
        
    def closest_parallel(self):
        return round(self.latitude)
    
    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now
    
    def get_weather(self):
        weather = Weather(apikey='26631f0f41b95fb9f5ac0df9a8f43c92',lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90,90), longitude = uniform(-180,180))

# tokyo = Geopoint(latitude = 35.7, longitude = 139)
# print(tokyo.get_time())
# print(tokyo.get_weather())
# 
# brasil = Geopoint(-15,-47)
# print(brasil.get_time())
# print(brasil.get_weather())

# chisinau = Geopoint(47.032460, 28.787535)
# date = chisinau.get_weather()
# 
# point = Geopoint.random()
# print(point.get_time(), point.get_weather())
# 

