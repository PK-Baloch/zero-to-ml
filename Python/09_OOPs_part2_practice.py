# del Keyword:
            # used to delete object properties or object itself.
class Student:
    def __init__(self,n):
        self.name=n
s1=Student("Ali Murtaza")
print(s1.name)
del s1
# print(s1.name)   # Error because s1 object is deleted

# Private(like) atteributes and methods:
    # Private atteributes and methods are meant they are only used withen the class
    # and not accessable outside the class
    # To make an atteribute or method private we use __ before it like: self.__name=name
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_password=acc_pass
    def show(self):
        print(self.__acc_password)
        self.__helo()
    def __helo(self):        # Private method
        print("helo person")
a1=Account(28332,"ali222")
print(a1.acc_no)
#print(a1.__acc_pass)     # Error because acc.pass is a private member
a1.show()                 # but we can access this using methods                
#a1.__helo()              # Error Because helo is a private method
         
# Inheritance: when a child/drived class drives or inherit the properties from it parent/base class 
#              then this is called inheritance

class Car:
    colour="black"
    @staticmethod
    def start():
        print("Car is started")
    @staticmethod
    def stop():
        print("Car is stoped")
class ToyoTa_Car(Car):
    def __init__(self,name):
        self.name=name
Car1=ToyoTa_Car("Mehran")
print(Car1.name)
Car1.start()

# Types of Inheritance:
# 1. Single Inheritance
# 2. Multi level Inheritance
# 3. Multiple Inheritance

# 1. Single Inheritance: Inheritance in which a parent class inherit thier properties to child class
# Example: we have already done an example of this type of inheritance in above programme

# 2. Multi Level Inheritance: In this type of inheritance parent class inherit their properties to
# child class and this child class also inherit their properties to other sub child class

# Example:
class Car:
        @staticmethod
        def start():
            print("Car is Started")

class ToYoTa(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(ToYoTa):
    def __init__(self, type):
        self.type=type

Car1=Fortuner("Diesel")
Car1.start()

# Super():
         #Super() method is used to access method of parent class
# Example:
class Person:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     @staticmethod
     def test():
          print("method is called successfully")
class Student(Person):
     def __init__(self, marks, name, age):
          super().__init__(name, age)
          self.marks=marks
          super().test()
s1=Student(98,"Ali",22)
print(s1.name)          

# Class Method:
              #Genrally used when need to access class atteributes and genrally takes cls as an first argument
class Person:
     name="Ahmed"
     @classmethod
     def change(cls,name): # here basically we access class atteribute so we will use class method
          cls.name=name
          return name
print(Person.name) 
Person.change("Rashid")
print(Person.name)
# Note:
# instance method takes self arrg by default
# class method takes cls arrg by default
# static method takes no arrg by default because we don't want to access any obj or cls arrg

# @property: We use @property decorator on any method in the class to use the method as property.

# Feature	                 Method          	        Property (@property)

# 1.What it is	         A function inside a class	  A method wrapped to behave like an attribute
# 2.How to call  	     With parentheses ()	      Like an attribute, no parentheses needed
# 3.Purpose     	     Represents an action	      Represents a value/data (even if calculated)
# 4.Can access state?	 Yes, via self	              Yes, via self
# 5.Can modify           Only if called as            Yes, syntax stays the same (obj.attr)
#  logic later without   method (parentheses stay)
#  breaking API?		
class Student:
     def __init__(self,math,chem,phys):
              self.math=math
              self.chem=chem
              self.phys=phys
     @property
     def percentage(self):
            return (self.math+self.chem+self.phys)/3

std1=Student(96,89,90)
print(std1.percentage)
std1.math=92
print(std1.percentage)

# Polymorphism: When same thing is allowed to have different meanings according to context.
# Operator Overlowding: 
print(1+2) # to sum
print("QUEST"+" Uninversity") # to concatenate
print([2,5,6,7]+[8,9]) # merge

# # Dunder Functions:
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +" ,self.img,"j")
    def __add__(self,num2):         # dunder function
        New_real=self.real+num2.real
        New_img=self.img+num2.img
        result=Complex(New_real,New_img)
        return result
    def __sub__(self,num2):         # dunder function
        New_real=self.real-num2.real
        New_img=self.img-num2.img
        result=Complex(New_real,New_img)
        return result
num1=Complex(2,4)
num1.showNumber()
num2=Complex(1,3)
num2.showNumber()
num3=num1+num2
num3.showNumber()
num3=num1-num2
num3.showNumber()

# Let's Practice:
# Qno:1. define a class Circle to creat a circle with radius r using constructor
#        def a area method of class circle which calculate area and a perimeter method 
#        to calculate perimeter
class Circle:
    def __init__(self,raduis):
        self.raduis=raduis
    def area(self):
        return (22/7)*self.raduis*self.raduis
    def perimeter(self):
        return 2*(22/7)*self.raduis
    
c1=Circle(6)
print(c1.area())
print(c1.perimeter())

# Creat a class employ that has atteributes role , dept and salary. This class also has
# a show method to desplay details
class Employ:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showDetails(self):
        print("Role of employ:",self.role)
        print("dept of employ:",self.dept)
        print("sal of employ:",self.sal)
class Engneer(Employ):
    def __init__(self, name,age):
        super().__init__("Manager", "IT",500000)
        self.name=name
        self.age=age
e1=Employ("Teacher","Information Tech",250000)
e1.showDetails()
eng=Engneer("name",30)
eng.showDetails()

# Creat a class Order which stores price and it's iotem 
# use dundar function __gt__() to convay that
# order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self,iotem,price):
        self.iotem=iotem
        self.price=price

    def __gt__(self,o2):
        return self.price>o2.price
    
o1=Order("chips",20)
o2=Order("biscket",30)
print(o1>o2)
