class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("This animal doesn't have a specific sound.")

class Dog(Animal):
    def make_sound(self):
        print("Bow!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")
        
name = input("Enter the name of the dog: ")
species = "Canis familiaris"
dog = Dog(name, species)
dog.make_sound()

name = input("Enter the name of the cat: ")
species = "Felis catus"
cat = Cat(name, species)
cat.make_sound()
