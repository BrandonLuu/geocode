import googlemaps

API_KEY = "AIzaSyC21X6viw2CyUsxj_IK5b0G7jhB0nmSd6E"

gmaps = googlemaps.Client(key=API_KEY)

# Geocoding and address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#geocode_result = gmaps.geocode("American Canyon Walmart Supercenter 7011 Main Street")
#geocode_result = gmaps.geocode("7011 Main Street American Canyon CA")
geocode_result = gmaps.geocode("800 Commerce Ave, Atwater, CA"
                               "")
print(geocode_result[0]['geometry']['location'])
