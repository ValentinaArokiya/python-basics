# INHERITANCE:
# FORMING NEW CLASSES USING CLASSES THAT HAVE ALREADY BEEN DEFINED
# HELPS TO RE-USE CODE

#### BASE CLASS:
class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")



my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

print("********************************")
# Dog class inherits from Animal class:
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()

print("**********CAT CLASS*****************")
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")


my_cat = Cat()
my_cat.who_am_i()
my_cat.eat()

#
###############################################################################################################

# # TEST PROGRAM:
#
# class Animal:
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def who_am_i(self):
#         print("I am animal")
#
#     def eat(self):
#         print("I am eating")
#
#
# my_animal = Animal()
# my_animal.who_am_i()
# my_animal.eat()
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
# my_dog = Dog()
# my_dog.who_am_i()
# my_dog.eat()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
