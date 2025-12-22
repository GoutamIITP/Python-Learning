# OOPs: Classes and Methods in Python

"""
There are three type of methods in Python OOPs:
1. Instance Methods
2. Class Methods
3. Static Methods
"""
# class Student:
#     school_name = "ABC High School"  # Class variable
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # Instance Method
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
    
#     # class Method
#     @classmethod
#     def get_school_name(cls):
#         return cls.school_name
    
#     # Static Method
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
    
# x = Student("John", 20)
# x.display()  # Instance method call
# print(x.get_school_name())  # Class method call

# print(x.is_adult(16))  # Static method call
# print(x.is_adult(20))  # Static method call


"""
object Composition in Python OOPs:
Composition is a design principle in object-oriented programming where a class is composed of one or more objects from other classes. This allows for building complex types by combining simpler, reusable components."""
# class Engine:
#     def __init__(self):
#         self.power = 150  # horsepower

#     def start(self):
#         print("Engine started with power:", self.power)

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition: Car has an Engine
     
#     def move(self):
#         self.engine.start()
#         print("Car is moving")


# c = Car()
# c.move()  # Using the composed object

"""
Inner Classes in Python OOPs:
An inner class is a class defined within another class. Inner classes can be used to logically group classes that are only used in one place, which increases encapsulation and helps to keep the outer class cleaner."""

class Outer:
    def __init__(self):
        self.x = 10

    class Inner:
        def __init__(self):
            self.y = 20

        def display(self):
            print("Inner class y value:", self.y)
    
    def outer_display(self):
        print("Outer class x value:", self.x)

out = Outer()
in_ = out.Inner()  # Creating instance of Inner class