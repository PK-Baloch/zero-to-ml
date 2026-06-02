"""# Lists:---> A list in Python is smilar to arrays in other languages.
#      ---> It can stor many values of same data type as well different data types.
#      ---> Lists are mutable (means we can chage its value at a spacific index).
marks=[45, 50, 53, 24, 89,78]
print(marks)
print(marks[0])
print(type(marks))
print(len(marks))

student=["Imran Ali",23,4.0,"Hyderabad"]
print(student)

# Slicing: The concept of slicing in list is same as in strings.
print(student[2:4])

# List methods:
list=[3,5,4,2]
# 1: list.append:
list.append(6)
print(list)

# 2: list.sort:
list.sort() # list is automaticaly sorted in asending order.
print(list)
list.sort(reverse=True) # list is sorted in decending order.
print(list)
list=['w','e','a','b','i'] 
list.sort() # list.sort function also works for strings.
print(list)

# 3: list.insert:
list1=[2,4,1,5,1]
list1.insert(1,3) # this funct assign value in list  to a particular index: list.insert(index,val)
print(list1)

# 4: list.remove:
list1.remove(1)
print(list1) # This funct will remove first occurence of element in list.

# 5: list.pop:
list1.pop(4) #This funct is smilar to remove method but it will remove an element at index.
print(list1)

# Tupple: It is a built in data type in python which is smilar to list that let us creat an immutable sequince of values.
tup=(80,38,93,87)
# tup[0]=40 => assignment is not allowed in tupple.
print(tup[0])
print(type(tup))
tup2=() # valid in python
tup3=(1) # valid but will treat as an integer
print(type(tup3))
tup3=(1,) # Now this will be considerd as tupple.
print(type(tup3))
tup4=() # An empty tupple is also valid.
print(tup4)
print(type(tup4))

# Slicing: It works same like string and list in tupple.
print(tup[0:2])

# Tupple methods:
# 1:tup.index:It returns index of first occurence of  an element in tupple.
tup=(3,4,2,5,4)
print(tup.index(4))

# 2:tup.count:It counts total occurence of an element in tupple.
print(tup.count(3))

#Lets Practice:
# 1: WAP to ask a user to enter the names of thier 3 favorite movies and store them in a list.
movies=[]
mov=movies.append(input("enter your first fav movie name:"))
mov=movies.append(input("enter your second fav movie name:"))
mov=movies.append(input("enter your third fav movie name:"))
print(movies)"""

# 2: WAP to check if a list contains palindrome of elements.
list1=[1,3,2,3,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(list1==copy_list1):
    print("Palindrome")
else:
    print("Not a Palindrome")
list2=["racecar"]
list2_copy=list2.copy()
list2_copy.reverse()
if(list2==list2_copy):
    print("Palindrome")
else:
    print("Not a Palindrome")
list3=["m","a","a","n"]
list3_copy=list3.copy()
list3_copy.reverse()
if(list3==list3_copy):
    print("Palindrome")
else:
    print("Not a Palindrome")

# 3: WAP to count the number of students with the "A" grade in the following tupple.
grade=("D","C","B","A","B","A","A")
grade_count=grade.count("A")
print(grade_count)

#Store the above values in a list and sort them from "A" to "D".
grade=["D","C","B","A","B","A","A"]
grade.sort()
print(grade)