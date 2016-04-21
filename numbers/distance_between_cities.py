"""
find 'as the crow flies' distance between two locations
using the google maps geocode api.

credit to michael-dunn on stackoverflow for the haversine
equation. http://stackoverflow.com/a/4913653/5130898

author: chrisitan scott
"""

from math import radians, cos, sin, asin, sqrt
from urllib2 import urlopen
import json

def check_response_status(*repsonses):
    statuses = []
    for repsonse in repsonses:
        if repsonse['status'] == 'OK':
            statuses.append(False)
        elif repsonse['status'] == 'REQUEST_DENIED':
            statuses.append(1)
        elif repsonse['status'] == 'ZERO_RESULTS':
            statuses.append(2)
    return statuses

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r

def get_cities(api_key, city_1, city_2):
    city_1 = city_1.strip().replace(' ', '%20')
    city_2 = city_2.strip().replace(' ', '%20')

    request_1 = urlopen(
        'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' 
        % (city_1, api_key))
    request_2 = urlopen(
        'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' 
        % (city_2, api_key))
    response_1 = json.loads(request_1.read())
    response_2 = json.loads(request_2.read())

    statuses = check_response_status(response_1, response_2)

    for city, status in zip((city_1, city_2), statuses):
        if status == 1:
            print "Bad API key. Please try again."
            exit()
        elif status == 2:
            print "Could not find %s. Please try again." % (city)
            exit()
    
    lat_1, long_1 = (response_1['results'][0]['geometry']['location']['lat'], 
        response_1['results'][0]['geometry']['location']['lng'])
    lat_2, long_2 = (response_2['results'][0]['geometry']['location']['lat'], 
        response_2['results'][0]['geometry']['location']['lng'])

    name_1, name_2 = (response_1['results'][0]['formatted_address'], 
        response_2['results'][0]['formatted_address'])

    return lat_1, long_1, lat_2, long_2, name_1, name_2

def main():
    try:
        api_key = json.loads(open('api_keys.json').read())['googlemaps']
    except:
        api_key = str(raw_input("Please enter your google maps geocode API key: "))

    city_1 = str(raw_input("First city: "))
    city_2 = str(raw_input("Second city: "))

    lat_1, lng_1, lat_2, lng_2, name_1, name_2 = get_cities(api_key, city_1, city_2)
    distance = haversine(lat_1, lng_1, lat_2, lng_2)

    print("Distance between %s and %s as the crow flies is %.2fkm." % 
        (name_1, name_2, distance))

if __name__ == "__main__":
    main()
