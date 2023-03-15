import numpy as np
import math
from functions import make_html
from functions.alt_az import get_alt_az

# Inputs
constellation_name = input("Constellation: ").strip().lower().title()
date = input("Date (MM/DD/YY): ").strip().split("/")
time = input("Time (HH:MM:SS): ").strip().split(":")
month, day, year = (date[0]), (date[1]), str(int(date[2])+2000)
hour, minute, second = (time[0]), (time[1]), (time[2])
print(f"Calculating the visible range of {constellation_name} on {month}/{day}/{year} at {hour}:{minute}:{second}...")

def get_lst():
    # Calculate the decimal hour
    decimal_hour = hour + minute / 60 + second / 3600
    # Calculate the Julian Date
    a = math.floor((14 - month) / 12)
    y = year + 4800 - a
    m = month + 12 * a - 3
    julian_date = day + math.floor((153 * m + 2) / 5) + (365 * y) + math.floor(y / 4) - math.floor(
        y / 100) + math.floor(y / 400) - 32045
    # Calculate the Greenwich Mean Sidereal Time (GMST)
    gmst = 18.697374558 + 24.06570982441908 * (julian_date - 2451545.0) + 0.000026 * decimal_hour
    gmst = gmst % 24  # Reduce the GMST to within 0-24 hours
    # Calculate the Local Sidereal Time (LST) in radians
    lst = math.radians(15 * gmst)
    return lst

# Variables to display progress
i = 0
b_n = 0
def get_visible_range():
    global i
    global b_n
    lats = []
    longs = []
    b_n = len(np.arange(-90, 90.10, 0.10))
    for lat in np.arange(-90, 90.10, 0.10):
        alt, az = get_alt_az(constellation_name, 0, lat, year, month, day, hour, minute, second, i, b_n)
        i+=1
        if alt > 10:
            lats.append(lat)
    i = 0
    print()
    b_n = len(np.arange(-180, 180.10, 0.10))
    for lon in np.arange(-180, 180.10, 0.10):
        alt, az = get_alt_az(constellation_name, lon, max(lats), year, month, day, hour, minute, second, i, b_n)
        i+=1
        if alt > 10:
            longs.append(lon)
    return min(lats), max(lats), min(longs), max(longs)

if __name__ == '__main__':
    min_lat, max_lat, min_long, max_long = get_visible_range()
    print("\n"+f"The constellation {constellation_name} is visible from {min_lat} to {max_lat} degrees latitude and from {min_long} to {max_long} degrees longitude at {hour}:{minute}:{second} on {month}/{day}/{year}.")
    make_html.make_html(max_lat, min_long, min_lat, max_lat)
