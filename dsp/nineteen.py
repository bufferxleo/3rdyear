from geopy.geocoders import Nominatim

def get_loc_info(lat,long):
    geolocator=Nominatim(user_agent="location_info_app")
    location=geolocator.reverse((lat,long),language='en')
    add_details=location.address.split(',')
    # city=location.raw.get("address",{}).get("city","")
    # state=location.raw.get("address",{}).get("state","")
    # country=location.raw.get("address",{}).get("country","")

    return add_details[1],add_details[-1],add_details[3]

lat=37
long=-122

print(get_loc_info(lat,long))
