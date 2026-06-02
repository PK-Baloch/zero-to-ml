#Loops:loops are used to repeat instructions.
# 1: While Loop: while condition:
#                   do something
"""count=1
while count<=5:
    print("hello world")
    count +=1
# print numbers from 1 to 5;
i=1
while i<=5:
    print(i)
    i+=1
# print numbers from 5 to 1;
i=5
while i>=1:
    print(i)
    i-=1

# Lets Practice:
# 1: print numbers from 1 to 100.
count=1
while count<=100:
    print(count)
    count +=1

# 2: print numbers from 100 to 1.
count=100
while count>=1:
    print(count)
    count -=1

# 3: print multiplication table of a numbr n.
table=int(input("enter table you want to print:"))
i=1
while i<=10:
    print(i*table)
    i+=1

# 4: print the elements of the following list using a loop.
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

# 5: Search for a number in the list using loop.
tupple1=(1,4,9,16,25,36,49,64,81,100)
a=0
x=int(input("enter the number:"))
while a<len(tupple1):
    if (tupple1[a]==x):
        print("Found at index:",a)
    a+=1 

# BREAK & CONTINUE:
# BREAK: used to terminate the loop when encountered.
tupple1=(1,4,9,16,25,36,49,64,81,100)
a=0
x=int(input("enter the number:"))
while a<len(tupple1):
    if(tupple1[a]==x):
        print("Found at index:",a)
        break
    else:
        print("finding")
    a+=1 
# Continue: terminates the execution in the current iteration and continues execution of the loop with next iteration.
i=0
while i<=10:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
# skip even numbers and print odd nums:
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1"""
""" for loop: for loop is used for sequential traversal. for traversing list,tupple,string etc.
for loop syntex:
list[1,5,3,6]
for el in list:
    do something
else:
    do something after loop"""
"""List=[1,3,5,7,9]
for el in List:
    print(el)
tup=(2,4,14,5,34,5)
for num in tup:
    print(num)
str="quetuniversity"
for char in str:
    print(char)"""
"""# WAP for an electrical circuit in which there is a fan which have to switches one on the ground floor
# and other on first floor , the fan is on when any one of the switch is on and it is off if both are off or on.
switch1=input("enter on or off switch1:").lower()
switch2=input("enter on or off switch2:").lower()
if(switch1=="on" and switch2=="on"):
    outp=False
elif(switch1=="on" or switch2=="on"):
    outp=True
else:
    outp=False

print(outp)

# Range():
# Range function returns a sequence of numbers starting from 1 ( by default ) and increament of 1 
# ( by default ) and stops before a specefied number.
# Syntex:
# Range(start(optional),stop,step(optional))

for el in range(3):
    print(el)

for el in range(1,9):
    print(el)

for el in range(0,10,2):
    print(el)
# WAP to search a number in an arr by linear search.
arr1=[23,93,43,53,83,73,63,33]
indx=0
for el in arr1:
    if(el==33):
        print("Found at index:",indx)
        break
    else:
        print("Finding")
    indx+=1

# Lets Practice:
# 1. WAP to find the sum of first n numbers:
n=int(input("enter the number "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print("Sum of first",n,"numbers is: ",sum)
"""

# Search an element in array using binary search .


def binary_search(arr,target):
    start=0
    end=len(arr)-1
    mid=(start+end)/2
    while(start<=end):
        if(target<mid):
         end=mid-1
        elif(target>mid):
         start=mid+1
    else:
       return mid
    


arr=[2,4,6,8,10,12,14]
target=float(input("enter your target: "))  
value=binary_search(arr,target)
print("Target is found at index no:",value)
        
    

# 2. WAP to calculate fact of n nums:
# n=int(input("enter a num :"))
# fact=1
# for i in range(n):
#     i+=1
#     fact=fact*i
# print("The fact of ",n,"nums is: ",fact)

