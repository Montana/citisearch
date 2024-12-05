import requests
import folium
from folium import plugins

STATION_STATUS_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
STATION_INFO_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"

def fetch_live_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def create_map_with_cross_lines(stations):
    nyc_map = folium.Map(location=[40.730610, -73.935242], zoom_start=12)

    for station in stations:
        folium.Marker(
            location=[station['latitude'], station['longitude']],
            popup=f"<b>{station['name']}</b><br>Available Bikes: {station['bikes']}",
            icon=folium.Icon(color='blue', icon='bicycle')
        ).add_to(nyc_map)

    for i in range(len(stations)):
        for j in range(i + 1, len(stations)): 
            start = stations[i]
            end = stations[j]
            folium.PolyLine(
                [[start['latitude'], start['longitude']], [end['latitude'], end['longitude']]],
                color="gray",
                weight=1,
                opacity=0.5
            ).add_to(nyc_map)


plugins.MiniMap().add_to(nyc_map)

    nyc_map.save("citi_bike_map_with_cross_lines.html")
    print("Map with cross-referencing lines saved as 'citi_bike_map_with_cross_lines.html'.")

def main():
    print("Fetching live Citi Bike data...")
    station_status = fetch_live_data(STATION_STATUS_URL)
    station_info = fetch_live_data(STATION_INFO_URL)

    stations = []
    status_data = {s['station_id']: s['num_bikes_available'] for s in station_status['data']['stations']}
    for info in station_info['data']['stations']:
        station_id = info['station_id']
        name = info['name']
        lat = info['lat']
        lon = info['lon']
        bikes = status_data.get(station_id, 0)
        stations.append({'name': name, 'latitude': lat, 'longitude': lon, 'bikes': bikes})

    create_map_with_cross_lines(stations[:50])  #y

if __name__ == "__main__":
    main()
