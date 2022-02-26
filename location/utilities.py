from geopy.geocoders import Nominatim
import time 


app = Nominatim(user_agent="google")
def location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return location_by_address(address)



def address_by_location(latitude, longitude):
    cordinates = f"{latitude},{longitude}"
    time.sleep(1)
    try:
        return app.reverse(cordinates, language="en")
    except:
        return address_by_location(latitude, longitude)



    