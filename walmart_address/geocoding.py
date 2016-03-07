"""
Author: Brandon Luu
Date: 2/22/16
Description: This script reads a file with newline separated addresses and into its lat/long
position and then writes all of these values into a CSV output file.
"""
import googlemaps

API_KEY = <API_KEY_GOES_HERE>

gmaps = googlemaps.Client(key=API_KEY)

# Input/Output file names
input_file = "Test_CA_city_list.csv"
output_file = "Test_CA_GPS_list.csv"

# Open files
in_fd = open(input_file, 'r')
out_fd = open(output_file, 'w')

# Find GPS of address
for line in in_fd:
    str = line + ",CA"
    print(str)
    """
    geocode_result = gmaps.geocode(str)
    Gps_lat = geocode_result[0]['geometry']['location']['lat']
    Gps_lng = geocode_result[0]['geometry']['location']['lng']

    # Write Address and GPS in CSV
    address = line[0:len(line)-1] # Remove newline
    Gps_string = '"%s",%s,%s\n' % (address, Gps_lat, Gps_lng)
    # print(Gps_string)
    out_fd.write(Gps_string)
    """
# Close Files
in_fd.close()
out_fd.close()
