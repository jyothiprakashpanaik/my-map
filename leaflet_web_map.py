import folium
import pandas

data = pandas.read_csv('stadium.csv',encoding="cp1252")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
capacity = list(data['capacity'])
website = list(data['website'])
picture = list(data['picture'])

fg = folium.FeatureGroup('my map')

for lt,ln,nm,cap,web,pic in zip(lat,lon,name,capacity,website,picture):
	fg.add_child(folium.Marker(location=[lt,ln],popup=f"<b>name: {str(nm)}</b> <b>capacity: {cap}</b> <b>Wekipedia Link: </b><a href={web}>click me</a> <b> <img src = {pic} height=142 width=290>",icon=folium.Icon(color = 'green')))


map=folium.Map(location=[17.4665, 78.4254],zoom_start=5)



fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("Leaflet.html")