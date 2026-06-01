"""
Strings and Conditional Statements Practice
Topics:
- String operations
- String methods
- If, elif, else
- Nested conditions
- Practice exercises
"""
str1="This is our first program.\nWe are doing it in Python." # \n ---> For next line
print(str1)
str1="This is our first program.\tWe are doing it in Python." # \t ---> For tab
print(str1)

#Basic Operations on Strings:
# 1: Concatenation: str1+str2
str1="QUEST "
str2="University"
print(str1+str2)

#Length of str:
len1=len(str1)
len2=len(str2)
print(len1)
print(len2)

#Indexing: In indexing we can find out the position of a single character in a string.
name="Asad Ali"
print(name[2])
name[4]="@" #error: we can not replace or manuplate by indexing. Only can be access.
print(name)

#Slicing: Accessing part of string.
name="QUEST University"
a=name[0:5]
print(a)
a=name[ :5] # name[0:5]
b=name[6: ] # name[6:len(str)]
print(a)
print(b)
# Negative Slicing:
a="APPLE" # -5 <---- -1
print(a[-5:len(a)])

#String Functions:

# 1:str.endswith():
str="I am a coder."
a=str.endswith("er.") #Return True if str ends with er., otherwise it will return False.
print(a)

# 2:str.capitalize():
str="i am a student of quest university nawabshah."
print(str.capitalize()) #it will make a copy of str and capitalize first latter but it will not be permenently capitalized.
print(str)
str=str.capitalize() # for permenent captalization we can store it in a variable.
print(str)

# 3:str.replace():
str="I am studeing python from ApnaCollage."
print(str)
print(str.replace("o","a"))
print(str)
print(str.replace("python","Javascripte"))

# 4:str.find(): This function finds our word in a str , where it occur it returns first index of first occur.
str1="I am Mr Piyaro Khan Shar."
print(str1.find("a"))

# 5:str.count(): This function count a substr in a str that how much times it is used in a str.
str2="I am from studeing python from apnacollage."
print(str2.count("a"))

# Lets Practice:
# 1: WAP to input user's first name and print it's length
name=input("enter your first name:")
print("length of your name is: ",len(name))

# 2: WAP to count occorance of $ in a str:
str3="Hi ,$ I am symbol of $   100.99$"
print(str3.count("$"))

# Conditional Statements:
# if,elif and else:
age=16
if(age>18):
    print("Can vote and apply for license.")
elif(age>15):
    print("Can drive")
else:
    print("you are still child")

#Traffic light signal:
light=input("enter traffic light color:")
if(light=="green"):
    print("Go")
elif(light=="red"):
    print("Wait")
elif(light=="Yellow"):
    print("Look")
else:
    print("light is brooken")

# Grade students based on marks:
marks=int(input("enter marks:"))
if(marks>=90 and marks<=100):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>=60 and marks<70):
    grade="D"
else:
    grade="F"
print("Your grade is: ",grade)

#Nesting:
age=int(input("enter your age:"))
if(age>=18):
    if(age>=85):
        print("you can not drive.")
    else:
        print("you can drive.")
else:
    print("you can not drive.")

#Let Practice:
# 1: WAP to check if a number provide by user is odd or even:
num=int(input("enter a num:"))
if(num%2==0):
    print("Your num is even.")
else:
    print("Your num is odd.")

# 2: WAP to find greatest of 3 numbers entered by user:
a=int(input("enter your first num:"))
b=int(input("enter your second num:"))
c=int(input("enter your third num:"))
if(a>b and a>c):
    print("The first number  is the greatest number.",a)
elif(b>c):
    print("The second number  is the greatest number.",b)
else:
    print("The third number is the greatest number.",c)

# HW: WAP to find greatest of 4 numbers entered by user:
a=int(input("enter your first num:"))
b=int(input("enter your second num:"))
c=int(input("enter your third num:"))
d=int(input("enter your fourth number:"))
if(a>b and a>c and a>d):
    print("The first number  is the greatest number.",a)
elif(b>c and b>d):
    print("The second number  is the greatest number.",b)
elif(c>d):
    print("The third number is the greatest number.",c)
else:
    print("The fourth number is the greatest number.",d)

# 3: WAP to check if a number is multiple of 7 or not:
number=int(input("enter a number: "))
if number % 7 == 0:
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")
