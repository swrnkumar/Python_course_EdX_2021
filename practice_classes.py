# practice exercises for classes - data structures

class Coordinate(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)


c = Coordinate(4,3)
origin = Coordinate(0,0)

print (c, origin)

print(c.distance(origin))

result_coordinates = Coordinate.distance(c,origin)

print(f"The distance between {c} and the origin {origin} is {result_coordinates}")

print(c, type(c))
print(Coordinate, type(Coordinate))

print(isinstance(c, Coordinate))
print(isinstance(origin, Coordinate))
print(isinstance(c.distance, Coordinate))
print(c.distance, type(c.distance))

foo = c - origin

print(foo)


class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = "6.30"
        print(self.time)

clock = Clock('5.30')
# clock.print_time("10.30")

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()


