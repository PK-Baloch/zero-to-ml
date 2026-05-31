# Python Basics Practice
# Topics: Operators, Type Conversion, Input/Output, and Practice Problems
#Arithamatic Operators
a=5
b=3
print(a-b) #difference
print(a+b) #sum
print(a*b) #multiplication
print(a/b) #devision

#Relational Operators
print(a==b) #False
print(a!=b) #True
print(a>b)  #True
print(a>=b) #True
print(a<b)  #False
print(a<=b) #False

#Assignment Operators
a=b
print(a)
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)

#Logical Operators: we have three logical operators Not,AND,OR
print(not (a<b))
val1=True
val2=False
print("AND Operator",val1 and val2)
print("OR Operator ",val1 or val2)
print((a==b)or(a>b))

#Type Conversion:
a=2
b=3.0
print(a+b)

#Type Casting:
a=float("3")
print(type(a))
print(a+b)
# c=int("Shar") // error

#INPUT IN PYTHON:
name=input("enter your name: ")
print("Wellcome",name)
print(type(name),name) #input has  string type by default but it can be farcast into int ,float and etc.
age=int(input("enter your age: "))
print(type(age))

#Practice Problem: WAP to input 2 numbers and print thier sum.
a=int(input("enter num1:"))
b=int(input("enter num2:"))
print("The sum of two numbers is: ",a+b)

#Practice Problem2: WAP to input side of squar and print its area:
a=int(input("enter side of squar: "))
print("The area of squar is: ",a*a)

#Practice Problem3: WAP to input two floating numbers and print thier average:
a=float(input("enter num1:"))
b=float(input("enter num2:"))
avg=(a+b)/2
print("The avg of two floating numbers is: ",avg)

#Practice Problem4: WAP to input two integer numbers a and b, print True if a is greater than or equal to b, otherwise False:
a=int(input("enter first num:"))
b=int(input("enter second num:"))
print(a>=b)
a=int(input("enter first no:"))
b=int(input("enter sec no:"))
print(a>=b)
