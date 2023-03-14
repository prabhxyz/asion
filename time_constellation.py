import make_html
from alt_az import get_alt_az

# Inputs
constellation_name = input("Constellation: ").strip().lower().title()
date = input("Date (MM/DD/YY): ").strip().split("/")
time = input("Time (HH:MM:SS): ").strip().split(":")

# Dictionaries to save data
longs = []
lats = []
not_in_range_lats = []

i = 0
for lat in range(-90, 91):
    alt, az = get_alt_az(constellation_name, 0, lat, int(date[2])+2000, (date[0]), (date[1]), (time[0]), (time[1]), (time[2]), i)
    i+=1
    if alt > 2:
        lats.append(lat)
    else:
        not_in_range_lats.append(lat)

if len(lats) == 0:
    print("No latitudes found")
else:
    print("\n"+f"Latitudes ({min(lats)} to {max(lats)}):")
    make_html.make_html(-180, 180, min(lats), max(lats))