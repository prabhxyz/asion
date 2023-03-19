#############################################################################################################
# This is a copy of https://raw.githubusercontent.com/prabhxyz/astro-coordination/main/celestial_direction.py
#############################################################################################################

import datetime
import numpy as np
import requests
import urllib.parse
from data.variables import ra_dict, dec_dict

# Get the current date and time
currentDateAndTime = datetime.datetime.now()
year=currentDateAndTime.year
month=currentDateAndTime.month
day=currentDateAndTime.day
hour=currentDateAndTime.hour
minute=currentDateAndTime.minute
second=currentDateAndTime.second
longitude=-0
latitude=0

# Set the longitude and latitude of the location (Normally)
location = input("Observer Location (Address): ")
def lonlat(address):
    global longitude
    global latitude
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    longitude = float(response[0]["lon"])
    latitude = float(response[0]["lat"])
lonlat(location)

# Calculate the Local Sidereal Time
def calculate_lst(longitude: float, date: datetime.date, time: datetime.time) -> datetime.time:
    # Convert the date and time to a datetime object
    dt = datetime.datetime.combine(date, time)
    # Convert the datetime object to UTC
    dt_utc = dt.astimezone(datetime.timezone.utc)
    # Calculate the number of days since J2000
    jd = 367 * dt_utc.year - int((7 * (dt_utc.year + int((dt_utc.month + 9) / 12))) / 4) + int((275 * dt_utc.month) / 9) + dt_utc.day - 730530
    # Calculate the Greenwich mean sidereal time (GMST) in hours
    gmst = 6.697375 + 0.0657098242 * jd + dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600
    # Shift GMST to LST using the local longitude
    lst = gmst + longitude / 15
    # Normalize LST to the range [0, 24)
    lst = lst % 24
    return lst

# Required parameters for the main functions
# Local Sidereal Time
lst = 15*(calculate_lst(longitude, datetime.date(currentDateAndTime.year, currentDateAndTime.month, currentDateAndTime.day), datetime.time(currentDateAndTime.hour, currentDateAndTime.minute, currentDateAndTime.second)))
def calc_alt(latitude, ra, lst, dec):
    ha = lst - ra  # hour angle
    alt = np.arcsin(np.sin(dec*np.pi/180) * np.sin(latitude*np.pi/180) + np.cos(dec*np.pi/180) * np.cos(latitude*np.pi/180) * np.cos(ha*np.pi/180))
    return alt*180/np.pi

def calc_az(dec, ha, lat):
    sin_dec = np.sin(np.deg2rad(dec))
    sin_lat = np.sin(np.deg2rad(lat))
    sin_ha = np.sin(np.deg2rad(ha))
    cos_dec = np.cos(np.deg2rad(dec))
    cos_lat = np.cos(np.deg2rad(lat))
    cos_ha = np.cos(np.deg2rad(ha))
    alt = np.arcsin(sin_dec * sin_lat + cos_dec * cos_lat * cos_ha)
    alt = np.rad2deg(alt)
    a = (sin_dec - np.sin(np.deg2rad(alt)) * sin_lat) / (np.cos(np.deg2rad(alt)) * cos_lat)
    a = np.arccos(a)
    a = np.rad2deg(a)
    if sin_ha < 0:
        return a
    else:
        return 360 - a

north = []
east = []
south = []
west = []

for key, val in ra_dict.items():
    # Right Ascension
    ra_hour = float(ra_dict[key][0:2])
    ra_minute = float(ra_dict[key][4:6])
    ra_second = float(ra_dict[key][8:10])
    ra = 15 * (ra_hour + ra_minute/60 + ra_second/3600)
    # Declination
    dec_hour = float(dec_dict[key][0:3])
    dec_minute = float(dec_dict[key][4:6])
    dec_second = float(dec_dict[key][8:10])
    dec = dec_hour + (dec_minute/60) + (dec_second/3600)
    alt = calc_alt(latitude, ra, lst, dec)
    az = calc_az(dec, lst - ra, latitude)
    print(f"{key}, Altitude: {alt}, Azimuth: {az}")
    if 0 < alt:
        if 315 < az < 0 or 0 < az < 45:
            north.append(key)
        elif 45 < az < 90 or 90 < az < 135:
            east.append(key)
        elif 135 < az < 180 or 180 < az < 225:
            south.append(key)
        elif 225 < az < 270 or 270 < az < 315:
            west.append(key)

print(f"\n---------------------North Constellations:")
for n in north:
    print(n)
print(f"\n---------------------East Constellations:")
for e in east:
    print(e)
print(f"\n---------------------South Constellations:")
for s in south:
    print(s)
print(f"\n---------------------West Constellations:")
for w in west:
    print(w)