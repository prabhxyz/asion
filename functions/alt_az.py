from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle
from astropy.time import Time
from data.variables import ra_dict, dec_dict
import sys

def get_alt_az(constellation_name: str, longitude: float, latitude: float, year: str, month: str, day: str, hour: str, minute: str, second: str, i: int, b_num:int):
    # Observer's location
    obs_location = EarthLocation(lat=latitude, lon=longitude, height=0)
    # Celestial object's coordinates
    celestial_object = SkyCoord(ra_dict[constellation_name], Angle(dec_dict[constellation_name], unit='degree'))
    # Time of observation
    obs_time = Time(f'{year}-{month}-{day}T{hour}:{minute}:{second}')
    # Calculate alt-az coordinates
    altaz = celestial_object.transform_to(AltAz(obstime=obs_time, location=obs_location))
    sys.stdout.write('\r' + f"Loading... {(i / b_num) * 100}%")
    return altaz.alt.deg, altaz.az.deg