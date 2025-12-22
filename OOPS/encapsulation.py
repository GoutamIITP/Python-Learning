"""
Docstring for OOPS.encapsulation:
Encapsulation in Python OOPs:
Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit or class. Encapsulation helps to restrict direct access to some of an object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
"""
# Example of Encapsulation in Python OOPs
class Car:
    __price = 10000  # Private attribute

    def display_price(self):
        print(f"The price of the car is: ${self.__price}")
    
c1 = Car()
c1.display_price()  # Accessing the price via a public method

