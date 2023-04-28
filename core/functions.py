from geopy import distance


def calculate_distance(position1, position2):
    return distance.distance(position1, position2).km