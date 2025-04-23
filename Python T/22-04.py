# Class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

# Class 2
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print("Car brand:", self.brand, "| Color:", self.color)

# Class 3
class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def make_sound(self):
        print("The", self.animal_type, "makes a sound")

p1 = Person("Rathod", 21)
c1 = Car("supra", "red")
a1 = Animal("Dog")

p1.say_hello()
c1.show_details()
a1.make_sound()
