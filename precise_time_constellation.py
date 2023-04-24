from astropy.time import Time
from functions.precise_above_horizon import above_horizon
from functions.make_html import make_html

def p_constellation(constellation_name, accuracy, max_altitude, min_altitude, max_azimuth, min_azimuth, date, time):
    # Inputs
    constellation_name = constellation_name.strip().lower().title()
    print((accuracy.strip()))
    accuracy = 10 - (int(accuracy.strip()) - 1)
    max_altitude = int(max_altitude.strip())
    min_altitude = int(min_altitude.strip())
    max_azimuth = int(max_azimuth.strip())
    min_azimuth = int(min_azimuth.strip())
    date = date.strip().split("/")
    time = time.strip().split(":")
    month, day, year = (date[0]), (date[1]), str(int(date[2])+2000)
    hour, minute, second = (time[0]), (time[1]), (time[2])
    print(f"Calculating the visible range of {constellation_name} on {month}/{day}/{year} at {hour}:{minute}:{second}...")
    time_converted = Time(f"{year}-{month}-{day} {hour}:{minute}:{second}")

    # List of visible locations
    visible_locations = []
    # Progress Variables
    i = 0
    b_num = (len(range(-90, 91, accuracy)) * len(range(-180, 181, accuracy))) - 1
    for lat in range(-90, 91, accuracy):
        for lon in range(-180, 181, accuracy):
            if above_horizon(constellation_name, lat, lon, 0, time_converted, i, b_num, max_altitude, min_altitude, max_azimuth, min_azimuth):
                visible_locations.append((lat, lon))
            i += 1

    # Make the HTML file
    print()
    make_html(visible_locations)