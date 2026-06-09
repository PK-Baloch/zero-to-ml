"""
File Handling Practice in Python

Topics Covered:
- Opening files
- Reading files
- Writing files
- Appending files
- Using with statement
- Deleting files
- String replacement
- Searching in files
- Counting even numbers from file data
"""
# File I/O in Python:
# Python can be used to perform operations on files (read and write data)
# Types of all files:
# 1: Text File: .txt , .docx , .log , etc
# 2: Binary File: .mp4 , .mov , .png , .jpeg , etc

# Open , Read and Close the File:
# We have to open the file before reading or writing.
# Syntex:
#        f=open("file_name","mode")
#                   /         \
#      sample.txt <-           -> r: read mode
#      demo.docx                  w: write mode

# Example:
f=open("file.txt","r")
data=f.read()
print(data)
print(type(data))


line1=f.readline()
line2=f.readline()
print(line1)      
print(line2)
print(type(data))
f.close()

# Different Modes:
# 1. 'r': Open for reading (by defualt).
# 2. 'w': Open a file for writing, by truncating the file first(clear all data or text).
# 3. 'x': creat a new file and open it for writing.
# 4. 'a': open a file in writing mode and appending in the end of the file if exist.
# //when we open a file in a or w mode if a file there not exist it will Automatically creat it.
# 5. 'b': open a file in binary mode for example mp4, video etc
# 6. 't': open a file in text mode
# 7. '+': open a disk file for updating( reading and writing )

# With Syntex:
#             when we open file with (with syntex) 
# then it allow us to perform diff modes on it like read , write , etc
with open("demo.py","r") as f:
    data=f.read()
    print(data)      # In this syntex we do not close the file because it Automatically close the file
with open("demo.py","w") as f:
    data=f.write("hello i am updating this file.")
    print(data)

# Deleting a file : using os module
# A module (like a code libarary) is a file written by an other programmer 
# that generally has a function that we can use.
# Syntex:
#        import os
#   os.remove(file name)

# import os
# os.remove("Lec1_ApnaCollege.py")

# Lets Practice:

# 1. Create a new file "Practice.txt" using python , Add following data in it.

with open("Practice.txt","w") as f:
    f.write("Hi everyone how are you \nwe are learning file I/O\n")
    f.write("using java\nI like programming in java")
    
# 2. WAF that replaces all occurrences of "java" with "Python" in above file.
with open("Practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","Python")
print(new_data)
with open("Practice.txt","w") as f:
    f.write(new_data)

# 3. Search if the word "learning" exist in the file or not.

word="learning"
with open("Practice.txt","r") as f:
    data=f.read()
    if(data.find(word) !=-1):
        print("Found")
    else:
        print("Not Found")

# 4. WAF to find in which line of the file does the word "learning" occur first , 
# print -1 if the word does not exist.
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                return line_no
            line_no+=1
    return -1
print(check_for_line())

# 5. From a file containing numbers saperated by comma ,
#  print the count of even numbers.
with open("Practice.txt","w") as f:
    data=f.write("2,3,4,6,5,48,55,43,24,56")
count=0
with open("Practice.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)
    
    
