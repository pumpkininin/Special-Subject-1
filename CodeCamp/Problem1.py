from math import radians, cos, sin, asin, sqrt

#The function haversine use to calculate distance of two point
# with the input is latitude and longitude
def haversine(lat_a, lat_b, long_a, long_b):
    # Radius of earth
    R = 6371
    d_latitude = radians(lat_a - lat_b)
    d_longitude = radians(long_a - long_b)
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    # Haversine formula
    distance = 2 * R * asin(sqrt(sin(d_latitude/2)**2) + cos(lat_a) * cos(lat_b) * sin(d_longitude/2)**2)
    return distance

def main():
    lat_a = float(input("Enter latitude of point A: "))
    long_a = float(input("Enter longtitude of point A: "))
    lat_b = float(input("Enter latitude of point B: "))
    long_b = float(input("Enter longitude of point B: "))
    # Call function haversine to calculate distance
    distance = haversine(lat_a,lat_b,long_a, long_b)
    print("Distance of point A and B is ", distance)


main()
