import math


class Point:

    # Initialize x, y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # calculate distance to origin
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


# Testcase:
if __name__ == "__main__":
    point_a = Point(1, 2)
    point_b = Point(4, 5)
    print(
        f"Point_a: {point_a.distance_to_origin()}, Point_b: {point_b.distance_to_origin()}"
    )
    print(math.sqrt(5), math.sqrt(41))
