
class Circle:
    #Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method:
    def area(self):
        print(self.pi * (self.radius**2))
    def get_circumference(self):
        return self.pi * self.radius * 2
    # self.pi can also be referenced as Circle.pi - since it is a Class Attribute.

my_circle = Circle(4)
print(my_circle.radius)
print(my_circle.pi)
(my_circle.area())
print(my_circle.get_circumference())
print(Circle.pi)



print(my_circle)

