"""
Author: Brandon Luu
Date: 3/6/16
Description: This script reads a list of CA cities and converts them into the GPS location given by Google.
A means to an end.
"""
import googlemaps
from time import sleep

API_KEY = "AIzaSyDq_JIEbzcsk-lRcC68drhYUtkC6R9HWOw"

gmaps = googlemaps.Client(key=API_KEY)

# Input/Output file names
# input_file = "full_school_list.csv"
input_file = "school_test.csv"
# output_file = "gps_sj_schools_test.csv"
output_file = "gps_school_test.csv"
# Open files
in_fd = open(input_file, 'r')
out_fd = open(output_file, 'w')

# Find GPS of address
for line in in_fd:
    city = "%s, San Jose CA" % line[:len(line)-1]
    print(city)

    geocode_result = gmaps.geocode(line)
    print(geocode_result)
    Gps_lat = geocode_result[0]['geometry']['location']['lat']
    Gps_lng = geocode_result[0]['geometry']['location']['lng']

    # Write Address and GPS in CSV
    address = line[0:len(line)-1] # Remove newline
    Gps_string = '"%s",%s,%s\n' % (address, Gps_lat, Gps_lng)
    print(Gps_string)
    out_fd.write(Gps_string)

# Close Files
in_fd.close()
out_fd.close()
