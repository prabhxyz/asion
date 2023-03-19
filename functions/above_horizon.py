import sys
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle
from data.variables import ra_dict, dec_dict

def above_horizon(constellation_name, latitude, longitude, height, time, i, b_num):
    # Define the position of the constellation
    constellation_name = constellation_name
    constellation_pos = SkyCoord(ra_dict[constellation_name], Angle(dec_dict[constellation_name], unit='degree'))

    # Define the location of the observer on Earth
    observer_lat = latitude
    observer_lon = longitude
    observer_height = height   # Elevation in meters
    observer_location = EarthLocation(lat=observer_lat, lon=observer_lon, height=observer_height)

    # Define the time of observation
    observation_time = time

    # Calculate the Altitude and Azimuth of the constellation at the given time and location
    constellation_altaz = constellation_pos.transform_to(AltAz(obstime=observation_time, location=observer_location))

    # Print progress
    sys.stdout.write('\r' + f"Loading... {(i / b_num) * 100}%")

    # Check if the constellation is visible above the horizon
    if constellation_altaz.alt.deg > 10:
        return True
    else:
        return False
