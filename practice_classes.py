import random
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


class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)

print(oneHalf)
print(twoThirds)

print(oneHalf.getNumer())
print(twoThirds.getDenom())

class ingSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found in set')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

s = ingSet()
print (s)
s.insert(23)
s.insert(90)
s.insert(8)
s.insert(23)
s.insert(764)
print(s)
print(s.member(765))
print(s.member(8))


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name = newname
    def __str__(self):
        return "animal: " + str(self.name) + ": " + str(self.age)

class cat(Animal):
    def speak(self):
        print("meowww")
    def __str__(self):
        return "cat: " + str(self.name) + ", " + str(self.age)

class rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: " + str(self.name) + ", " +str(self.age)

class person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello friends!")
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than ", other.name)
        elif self.age == other.age:
            print(self.name, "is the same age as", other.name)
        else:
            print(self.name, "is", -diff, "years younger than ", other.name)
    def __str__(self):
        return "person: " + str(self.name) + ", " +str(self.age)

class student(person):
    def __init__(self, name, age, major = None):
        person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I need to finish assignments")
        elif 0.25 <= r < 0.5:
            print("I need to eat")
        elif 0.5 <= r < 0.75:
            print("I need to sleep")
        else:
            print("I'm taking a break")
    def __str__(self):
        return "Student: " + str(self.name) + ", " + str(self.age) + ", studying " + str(self.major)
    

myanimal = Animal(3)
myanimal.set_name('foo')
myanimal.set_age(33)

jelly = cat(1)
jelly.set_name('foobar')
jelly.set_age(5)


blob = rabbit(7)
blob.set_name('fifee')
blob.set_age(7.5)

eric = person('Eric', 54)
eric.set_age(34)
bob = person('Bobbobb', 25)
das = person('dasss', 34)

print(myanimal)
print(myanimal.get_age())
print(myanimal.get_name())
print(jelly)
print(blob)
print(blob.speak())
print(jelly.speak())
print(eric.speak())
eric.age_diff(bob)
eric.age_diff(das)
person.age_diff(bob, das)
matt = student("matt", 16, "EdX course 1")
print(matt)
matt.speak()