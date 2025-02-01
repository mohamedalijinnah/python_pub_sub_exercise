# Sample program to demonstrate multiple publishers

def publish_geo_data():
    print("Publishing NL geo data")
    # Reference https://www.latlong.net/
    return (52.132633, 5.291266)

def get_geo_data_boundary():
    print("NL Latitude and Longitude boundary")
    # Reference https://latitudelongitude.org/nl/
    return (50.77083, 53.35917), (3.57361, 7.10833)

if __name__ == '__main__':
   print("Simulate a geo data publishers")