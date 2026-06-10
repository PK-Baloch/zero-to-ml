# OOP in Python:
# To map with real world senoireos , we starts objects in code.This is called Object Oriented Programming.
# Class and Object(Instances) in Python:
# Class:
# A class in python is a blueprint for creating objects.
# Creating a class:
#  class Student:
#     name="Ali Hyder" 
# Creating object:
# s1=Student()             
# print(s1.name)

# class Student:
#     name="Piyaro Khan"
# s1=Student()
# print(s1.name)

# Constructor:
# All classes have a function called __init__() , which is always executed when class is being initiated.

# Creating a class:                               Creating an Object:
#    class Student:                                  s1=Student("Ali Hyder")
#     def __init__(self,full_name):                  print(s1.name)
#        self.name=full_name 

# Default / Non Perametarized constructor:
class Student:
    def __init__(self):
        print(self)      # The self perameter is refference to the current object of the class,
                         #and is used to access the variable belongs to the class.
        print("hello i am a constructor.")
s1=Student()
print(s1) 

# Perametarized Constructor:
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("Mustafa Ali",92)
print(s1.name)
print(s1.marks)
s2=Student("Ghulamullah",83)
print(s2.name)
print(s2.marks)
# NB: There may be more than one constructor in the class and are envocked as according to perametors it is called constructor overlowding

# Class attributes:
# Those attributes which are linked with the class.
# these attributes can be used for every object in the class.
# They occupy space in memory only once.

# Object attributes:
# These attributes are linked with object.
class Student:
    Uni_name="QUEST NAWABSHAH" # class atteribute
    age=21
    def __init__(self,name,marks,age):
        self.name=name         # object atteribute
        self.marks=marks
        self.age=age           # object atteribute > class atteribute (object atteribute has higher percedence)
s1=Student("M Hassan",92,23)
print(s1.name,s1.marks,s1.age)

# Methods:
#         methods are basicaly fuctions that belongs to objects

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def wellcome(self):
        print(self.name,"hello students")
    def get_data(self):
        return self.marks
s1=Student("Omar",94)
s1.wellcome()
print(s1.get_data())

# Creat a class that takes name and marks of 3 subjects as arguments in a constructor
# and creat a method to print average
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def get_info(self):
        return (self.m1+self.m2+self.m3)/3
s1=Student("Meer Hadi",80,90,70)
print(s1.name)
print(s1.get_info())

# Static Methods:
#                Methods that don't use self perametor (work at class level)
# class Student:
#     @staticmethod        # Decorator
#     def hello():
#         print("hello guys")

# s1=Student()
# s1.hello()
# Decorator:
#           Decorator allow us to wrape an other function in order to extend the behavior of
#           the wraped function without permenantly modefing it

# 4 Pilors of OOPs:
# 1.Abstraction:
#               Hiding the implementation details of a class and showing only essential features to the user.
# Example:
# class Car:
#     def __init__(self):
#         self.accelerator=False  # hiding internal machanism of car 
#         self.clutch=False
#         self.Break=False
#     def start(self):
#         self.accelerator=True
#         self.clutch=True
#         print("Car started")
# car1=Car() 
# car1.start()                   # Giving only access to usefull features

# Encapsulation:
#               Wraping up data and methods into a single unit (object).
# Example : all above programms are examples of encapsulation where we collect data and functions and bound them in class.

# Lets Practice:
# Creat Account class with 2 atteributes balance and account no
# Creat method for debt , credit and printing balance

# class Account:
#     def __init__(self,bal,acc):
#              self.balance=bal
#              self.acc_no=acc
#     def debt(self,amount):
#          self.balance-=amount
#          print("The amount of ",amount,"was debted from your account")
#          print("Total Balance = ",self.get_balance())  
#     def credit(self,amount):
#          self.balance+=amount
#          print("The amount of ",amount," was credited to your account")
#          print("Total balance = ",self.get_balance())
#     def get_balance(self):
#          return self.balance 
# acc1=Account(10000,12356)   
# acc1.debt(1000)
# acc1.credit(500)
