from folium import Map
from geopoint import Geopoint
from timezonefinder import TimezoneFinder

latitude = float('40.09')
longitude = float('3.47')

antipode_latitude = latitude.__mul__(-1)

if(longitude.__lt__(float('0'))):
    antipode_longitude = longitude.__add__(180)
else:
    antipode_longitude = longitude.__sub__(180)

location = list((antipode_latitude, antipode_longitude))
mymap = Map(location)
mymap.save(str('antipode.html'))
mypoint = Geopoint(41.2,4.1)
print(mypoint.closest_parallel())

print(antipode_latitude,antipode_longitude,mymap, sep='\n')