from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle
from astropy.time import Time
from variables import ra_dict, dec_dict
from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")
# Get current location coordinates using geolocator and the device's IP address
address = input("Your address: ").strip().lower().title()
location = geolocator.geocode(address)
# Observer's location using geopy
latitude = location.latitude
longitude = location.longitude

obs_location = EarthLocation(lat=-latitude, lon=longitude, height=0)
# Celestial object's coordinates
constellation_name = input("Constellation: ").strip().lower().title()
celestial_object = SkyCoord(ra_dict[constellation_name], Angle(dec_dict[constellation_name], unit='degree'))

# Time of observation
obs_time = Time.now()

# Calculate alt-az coordinates
altaz = celestial_object.transform_to(AltAz(obstime=obs_time, location=obs_location))

# Print the altitude and azimuth in degrees
print('Altitude:', altaz.alt.deg, 'Azimuth:', altaz.az.deg)
