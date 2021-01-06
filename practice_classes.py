# practice exercises for classes - data structures

class Coordinate(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(4,3)
origin = Coordinate(0,0)

print(c.distance(origin))

result_coordinates = Coordinate.distance(c,origin)

print(f"The distance between {c} and the origin is {result_coordinates}")