import requests
from datetime import datetime, timedelta
from termcolor import colored

STATION_STATUS_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
STATION_INFO_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
RECENT_MINUTES = 5

def fetch_live_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(colored(f"Error fetching data: {e}", "red"))
        return None

def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def is_recent(timestamp):
    return datetime.fromtimestamp(timestamp) > datetime.now() - timedelta(minutes=RECENT_MINUTES)

def calculate_column_widths(data, headers):
    column_widths = [len(header) for header in headers]
    for row in data:
        for i, value in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(value)))
    return column_widths

def print_table(data, headers, title):
    column_widths = calculate_column_widths(data, headers)
    total_width = sum(column_widths) + len(headers) - 1

    print("\n" + "=" * total_width)
    print(f"{title:^{total_width}}")
    print("=" * total_width)

    header_row = " | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(headers))
    print(header_row)
    print("-" * total_width)

    for row in data:
        formatted_row = " | ".join(f"{str(value):<{column_widths[i]}}" for i, value in enumerate(row))
        print(formatted_row)

def print_station_status(data):
    stations = data.get('data', {}).get('stations', [])
    recently_returned = []
    station_data = []

    for station in stations:
        station_id = station.get('station_id')
        bikes_available = station.get('num_bikes_available', 0)
        docks_available = station.get('num_docks_available', 0)
        is_renting = "Yes" if station.get('is_renting') else "No"
        last_reported = station.get('last_reported')
        if last_reported is None:
            continue
        last_reported_str = format_time(last_reported)
        row = [station_id, bikes_available, docks_available, is_renting, last_reported_str]
        station_data.append(row)
        if bikes_available > 0 and is_recent(last_reported):
            recently_returned.append(row)

    print_table(station_data, ["Station ID", "Bikes", "Docks", "Renting", "Last Reported"], "Station Status")

    if recently_returned:
        print_table(recently_returned, ["Station ID", "Bikes", "Docks", "Renting", "Last Reported"], "Recently Returned")

def print_station_info(data):
    stations = data.get('data', {}).get('stations', [])
    station_info = []

    for station in stations:
        station_id = station.get('station_id')
        name = station.get('name', 'Unknown')
        lat = station.get('lat', 0.0)
        lon = station.get('lon', 0.0)
        row = [station_id, name, f"{lat:.6f}", f"{lon:.6f}"]
        station_info.append(row)

    print_table(station_info, ["Station ID", "Name", "Latitude", "Longitude"], "Station Information")

def print_header():
    print(colored("🚲🚲🚲 Citibike Live Tracker 🚲🚲🚲", "cyan", attrs=["bold"]))
    print("=" * 70)

def main():
    print_header()
    station_status = fetch_live_data(STATION_STATUS_URL)
    station_info = fetch_live_data(STATION_INFO_URL)

    if station_status:
        print_station_status(station_status)
    if station_info:
        print_station_info(station_info)

if __name__ == "__main__":
    main()

