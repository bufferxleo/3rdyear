from geopy.geocoders import Nominatim
def get_address(state):
    geolocator=Nominatim(user_agent="state_to_country_converter")
    location=geolocator.geocode(state)
    address=location.address if location else "not found"
    return address

state='California'
print(get_address(state).split(',')[1]) 