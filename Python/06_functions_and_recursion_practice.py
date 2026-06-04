# Functions:
# The block of code that perform a speciefic task.

# Syntex:
# def Func_name(param1,param2):  ----> Function Defination
#       do some work
#       return value
# Func_name(arg1,arg2)  ---->  Function Call

def calc_Sum(a,b):
    return a+b
print("The Sum is: ",calc_Sum(9,4))

def avg(p1,p2,p3):
    return (p1+p2+p3)/3
print("The avg of given nums is: ",avg(2,7,3))

# Functions in Python:
# 1: Builtin Functions:
#   Functions that are already defined in python are known as builtin functions.
# for exmp: print(), len(),rang(),lower(),etc
# 2: User Defined Functions:
#   Fuctions that are defined by user for its personal use are known as User Defined Fucntions

# Default Arguments:
# def calc_prod(a=1,b) //this will make through an error becuase default arg are written after non default arguments
def calc_prod(a=1,b=2):
    return a*b
print(calc_prod())

# Practice:
 
# WAP to print the len of a list , take list as an argument
def calc_len(l1):
    return len(l1)
list1=[2,5,2,6,5]
print("The len of given list is: ",calc_len(list1))

# WAP to print the elements of a list in a single line,(list as paramenter)
def print_el(l1):
    for el in l1:
        print(el,end=" ")
list1=[2,5,2,6,5]
print_el(list1)

# WAP to find the factorial of n numbers,(n as an arg);
def calc_fact(n):
    fact=1
    for el in range(1,n+1):
        fact*=el
    print("The fact of ",n," is: ",fact)
calc_fact(3)

# WAP to convert USD to PKR: lets 1 USD = 86 PKR
def convert_cur(usd_val):
    pkr_val=usd_val*280
    print(usd_val," usd = ",pkr_val,"pkr")
convert_cur(2)

# HOME WORK: WAF that return odd or even value depending upon user.
def func(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
n=int(input("enter a num:"))
print(func(n))  

# Recursion: When a function calls itself repeadily its known as recursion.

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(4)

def fact(n):
    if(n==0 or n==1):
        return 1      # This 1 will return where from it is being called.
    else:
        return n*fact(n-1)
print(fact(5))

# Lets Practice:
# 1: Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n==0):
        return 0
    else:
        return calc_sum(n-1)+n
print(calc_sum(10))

# 2: Write a recursive function to print the elements of a list.
# (hint: use list and indix)
def print_el(list,indx=0):
    if(indx==len(list)):
        return
    print(list[indx])
    print_el(list,indx+1)
fruits=["mango,banana,apple"]
print_el(fruits)
