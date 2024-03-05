# Filename: Pet.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that implemies Pet class and to create three instances of the class and print each object's attributes
# Last changed: 04-03-2024

# Program that implemies Pet class and to create three instances of the class and print each object's attributes
# Define the Pet class
class Pet:
    def __init__(self, name, animal_type, age):
        """
        Constructor to initialize a Pet object with name, animal type, and age.

        Args:
            name (str): The name of the pet.
            animal_type (str): The type of animal.
            age (int): The age of the pet.
        """
        self.name = name
        self.animal_type = animal_type
        self.age = age


# Creating instances of the Pet class
pet1 = Pet("Buddy", "dog", 3)
pet2 = Pet("Whiskers", "cat", 5)
pet3 = Pet("Tweety", "bird", 2)

# Printing each object's attributes
print("Pet 1:")
print("Name:", pet1.name)
print("Animal Type:", pet1.animal_type)
print("Age:", pet1.age)
print()

print("Pet 2:")
print("Name:", pet2.name)
print("Animal Type:", pet2.animal_type)
print("Age:", pet2.age)
print()

print("Pet 3:")
print("Name:", pet3.name)
print("Animal Type:", pet3.animal_type)
print("Age:", pet3.age)


# Description:
# The Pet class is defined to represent pets, with attributes such as name, animal type, and age.
# Instances of the Pet class (pet1, pet2, and pet3) are created with different attributes.
# Each object's attributes are printed using print() statements.
# Comments are added to describe the purpose of each section of the code, including the class definition and object creation.