import requests
import folium
from folium import plugins

STATION_STATUS_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
STATION_INFO_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"

def fetch_live_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def create_station_markers(stations, nyc_map):
    for station in stations:
        folium.Marker(
            location=[station['latitude'], station['longitude']],
            popup=f"<b>{station['name']}</b><br>Available Bikes: {station['bikes']}",
            icon=folium.Icon(color='blue', icon='bicycle')
        ).add_to(nyc_map)

def create_simple_lines(stations, nyc_map):
    for i in range(len(stations) - 1):
        start = stations[i]
        end = stations[i + 1]
        folium.PolyLine(
            [[start['latitude'], start['longitude']], [end['latitude'], end['longitude']]],
            color="blue",
            weight=4,
            opacity=0.8
        ).add_to(nyc_map)

def create_cross_lines(stations, nyc_map):
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

def create_map(stations, mode):
    nyc_map = folium.Map(location=[40.730610, -73.935242], zoom_start=12)

    create_station_markers(stations, nyc_map)

    if mode == 2:
        create_simple_lines(stations, nyc_map)
    elif mode == 3:
        create_cross_lines(stations, nyc_map)

    plugins.MiniMap().add_to(nyc_map)
    file_name = f"citi_bike_map_mode_{mode}.html"
    nyc_map.save(file_name)
    print(f"Map saved as '{file_name}'.")

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

    print("\nChoose a visualization mode:")
    print("1: Station markers only")
    print("2: Station markers with simple connecting lines")
    print("3: Station markers with cross-referencing lines")
    mode = int(input("Enter your choice (1, 2, or 3): "))

    if mode not in [1, 2, 3]:
        print("Invalid choice. Exiting.")
        return

    create_map(stations[:50], mode)  

if __name__ == "__main__":
    main()
