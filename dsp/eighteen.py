from geopy.geocoders import Nominatim
def get_address(lat,long):
    geolocator=Nominatim(user_agent="location_address_app")
    location=geolocator.reverse((lat,long),language='en')

    address=location.address if location else "not found"
    return address,type(address)

lat=37
long=-122

print(get_address(lat,long))