#!/usr/bin/env python3
"""
location.py - Command Line Location Finder
"""

import argparse
from geopy.geocoders import Nominatim

def get_location(place):
    geolocator = Nominatim(user_agent="location_script")
    location = geolocator.geocode(place)
    return location

def main():
    parser = argparse.ArgumentParser(description="Find latitude and longitude of any location")
    parser.add_argument("place", help="Name of the location")
    args = parser.parse_args()

    location = get_location(args.place)
    if location:
        print(f"\nLocation details for: {args.place}\n")
        print(f"Address   : {location.address}")
        print(f"Latitude  : {location.latitude}")
        print(f"Longitude : {location.longitude}")
    else:
        print("Location not found")

if __name__ == "__main__":
    main()
