from folium import Map, Marker, Popup
from geopoint import Geopoint
import pandas as pd

df = pd.read_excel('capitals.xlsx', engine='openpyxl')
narray = df.to_numpy()

#put all info of capital in var capital_location 
location = []
capital_location = []
for i in range(len(narray)):
    for j in range(5):
        location.append(narray[i][j])
    capital_location.append(location)
    location=[]

#Folium Map instance
mymap = Map(location = [25, 35],zoom_start = 3, max_zomm = 1)

for loc in capital_location:
    #Create a Geopoint instance
    geopoint = Geopoint(latitude=loc[0], longitude=loc[1])
    forecast = geopoint.get_weather()
    print(loc[0],loc[1])

    popup_content = f"""
    {loc[2]}
    <hr style="margin:0px">
    {forecast[0][0][-8:-6]}h: {round((forecast[0][1]-32)*5/9)}°C <img src='http://openweathermap.org/img/wn/{forecast[0][3]}@2x.png' width = 35>
    <hr style="margin:0px">
    {forecast[1][0][-8:-6]}h: {round((forecast[1][1]-32)*5/9)}°C <img src='http://openweathermap.org/img/wn/{forecast[1][3]}@2x.png' width = 35>
    <hr style="margin:0px">
    {forecast[2][0][-8:-6]}h: {round((forecast[2][1]-32)*5/9)}°C <img src='http://openweathermap.org/img/wn/{forecast[2][3]}@2x.png' width = 35>
    <hr style="margin:0px">
    {forecast[3][0][-8:-6]}h: {round((forecast[3][1]-32)*5/9)}°C <img src='http://openweathermap.org/img/wn/{forecast[3][3]}@2x.png' width = 35>
    <hr style="margin:0px">
    """

    #Create Popup object and it to Geopoint
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)


# Save the Map instance into a HTML file
mymap.save('map.html')

 
