# Filename: Person.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that creates three instances of the class using the def main() technique
# Last changed: 04-03-2024

# Program that creates three instances of the class using the def main() technique
class Person:
    def __init__(self, name, phone_number):
        """
        Initializes a Person object with a name and a phone number.

        Args:
            name (str): The name of the person.
            phone_number (str): The phone number of the person.
        """
        self.name = name
        self.phone_number = phone_number

def main():
    # Creating instances of the Person class
    person1 = Person("John", "123-456-7890")
    person2 = Person("Alice", "987-654-3210")
    person3 = Person("Bob", "456-789-0123")

    # Printing each object's attributes
    print("Person 1:")
    print("Name:", person1.name)
    print("Phone Number:", person1.phone_number)
    print()

    print("Person 2:")
    print("Name:", person2.name)
    print("Phone Number:", person2.phone_number)
    print()

    print("Person 3:")
    print("Name:", person3.name)
    print("Phone Number:", person3.phone_number)

if __name__ == "__main__":
    main()

# Desription:
# This Python script defines a Person class with attributes name and phone_number, representing a person's name and phone number respectively.
# The main() function creates instances of the Person class and prints out the name and phone number of each person.