"""
This program creates a 'Point' class and tests it. A point is basically a pair of x,y coordinates in
cartesian space. It has methods to add two points and to compute sthe distance between two points.

Note that this is a really basic example, a more comprehensive example is in point-class.py.

MF, Nov 2018

"""
import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def distance(self, other_point):
        if not isinstance(other_point, self.__class__):
            # raise TypeError("{} is not a valid Point object".format(str(other_point)))
            return "ERROR: {} is not a valid Point object".format(str(other_point))
        return math.sqrt(((abs(self.x - other_point.x)) ** 2) + ((abs(self.y - other_point.y)) ** 2))

    def sum(self, other_point):
        if not isinstance(other_point, self.__class__):
            return f"ERROR: {other_point} is not a valid Point object"
        return Point(self.x + other_point.x, self.y + other_point.y)



class MyClass:
    pass

def my_function():
    pass



if __name__ == "__main__":
    point1 = Point(2, 3)
    point2 = Point(4, 8)
    point3 = point1.sum(point2)
    int1 = 5

    print(point1, point2, point3)
    print("Distance from {} to {} is {}".format(point1, point2, point1.distance(point2)))
    print("Distance from {} to {} is {}".format(point1, int1, point1.distance(int1)))
