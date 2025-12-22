# Inheritance 
"""
Inheritance in Python OOPs:
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a subclass or derived class) to inherit attributes and methods from an existing class (called a superclass or base class). This promotes code reusability and establishes a hierarchical relationship between classes."""

# Single Inheritance
class A:
    def A(self):
        print("I am A")

class B(A):
    def B(self):
        print("I am B")

class C(B):
    def C(self):
        print("I am C")

obj = C()
obj.A()  # Inherited method from class A
obj.B()  # Method from class B
obj.C()  # Method from class C

# Inheritance Types Summary
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child1(Parent):
    def __init__(self, name, age, school):
        Parent.__init__(self, name, age)
        self.school = school

obj1 = Child1("Alice", 12, "Greenwood High")
print(f"Name: {obj1.name}, Age: {obj1.age}, School: {obj1.school}")