# #Example: 1
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)
print("________________________________________________________")


print("---------------The next one is also correct. But not the conventional method to follow------------------------------------------")

class Dog1:
    def __init__(self, breed):
        self.my_attribute = breed


my_dog = Dog1('Lab')
print(my_dog.my_attribute)

print("________________________________________________________")

class Dog:

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS. HENCE WE DO NOT USE THE 'SELF' KEYWORD.
    species = 'mammal'

    def __init__(self, breed, name, spots):

        ## ATTRIBUTES DEFINED WITHIN THE INIT METHOD VARIES FOR EACH INSTANCE OF THE CLASS. EACH INSTANCE HAS ITS OWN 'NAME,BREED AND SPOTS'.
        ## WE TAKE IN ARGUMENTS
        ## ASSIGN IT USING SELF.ATTRIBUTE_NAME
        #Expect string variables
        self.breed = breed
        self.name = name
        #Expect boolean True/False
        self.spots = spots

    # METHODS - OPERATIONS/ Actions:
    # you can also pass in an argument directly in the method. These arguments dont need the self keyword.
    def bark(self, number):
        print("WOOF!")
        print("WOOF! My name is {} and the number is {}" .format(self.name, number)) # you dont have to use'self' for number.


my_dog = Dog(breed='Lab', name='Sammy', spots=False)
# when you call an attribute, there is nothing to be executed.
# when you call a method on an object, the method has to be executed. Hence we use a '()' for the method calls.

print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(7))
print("0000000000000000000000000000000000000000000000000000000000000000000000000000")



