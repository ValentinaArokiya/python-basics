class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says WHOOF"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW"


niko = Dog("niko")

felix = Cat("felix")

print(niko.speak())

print(felix.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

