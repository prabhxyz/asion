from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle
from astropy.time import Time
from data.variables import ra_dict, dec_dict
from geopy.geocoders import Nominatim

# Get current location coordinates using geolocator and the device's IP address
line = int(input("Online: Enter 1\nOffline: Enter 2\nChoice: "))
if line == 1:
    address = input("Observer Address: ").strip().lower().title()
    # Initialize geolocator
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address)
    # Observer's location using geopy
    latitude = location.latitude
    longitude = location.longitude
elif line == 2:
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

obs_location = EarthLocation(lat=latitude, lon=longitude, height=0)
# Celestial object's coordinates
constellation_name = input("Constellation: ").strip().lower().title()
celestial_object = SkyCoord(ra_dict[constellation_name], Angle(dec_dict[constellation_name], unit='degree'))

# Time of observation
date = input("Date (MM/DD/YY): ").strip().split("/")
time = input("Time (HH:MM:SS): ").strip().split(":")
month, day, year = (date[0]), (date[1]), str(int(date[2])+2000)
hour, minute, second = (time[0]), (time[1]), (time[2])
obs_time = Time(f"{year}-{month}-{day} {hour}:{minute}:{second}")

# Print longitude and latitude
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

# Calculate alt-az coordinates
altaz = celestial_object.transform_to(AltAz(obstime=obs_time, location=obs_location))

# Print the altitude and azimuth in degrees
print('Altitude:', altaz.alt.deg, 'Azimuth:', altaz.az.deg)
