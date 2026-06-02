
# Dictionary: Dictionaries are used to store data values in "key":"value" pairs.
#They are unordered , mutable(changable) and don't allow duplicate keys.
Info={
"Name":"Hyder Ali",
"State":"Sindh",
"Number":34,
"marks":[85,83,23,39],
          "gpa":4.0,
}
print(Info)
print(Info["Name"]) # We can also excess dict elements indevidualy.
Info["Name"]="Asif Ali" # We can also change the value of key.
print(Info["Name"]) 
Info["Sur_name"]="Unar" # also can assign a new key.
print(Info["Sur_name"])

#Nested Dictionary:
Student={
    "Name":"Aqib Ali",
    "Subjects":{
        "Math":84,
        "chem":74,
        "Phys":83
    }
    
}

print(Student)
print(Student["Subjects"]) # We can also access only Subjects.
print(Student["Subjects"]["chem"]) # Can also access a particular element of dict.

# Dictionary Methods:
# 1: dict.keys(): returns all keys.
print(Student.keys())
print(list(Student.keys())) # Can also type cast in list or other data types.

# 2: dict.values(): returns all values.
print(list(Student.values()))

# 3: dict.items(): returns all (key,values) pairs as tupple.
print(Student.items())
pairs=list(Student.items()) 
print(pairs[0]) # Can individualy access a single pair also.

# 4: dict.get("key"): returns the key according to the value.
print("BEFORE")
#print(Student["Name2"]) #error: here above code will execute but below will not because of why we use methods
print("AFTER") 
print(Student.get("Name2")) # No error

# 5: dict.update(newdic): Insert the specified items to the dictionary.
new_dict={"city":"Nawabshah","age":18}
Student.update(new_dict)
print(Student)
new_dict={"Name":"Aman"} # If we insert same key then it will be overide and value will be changed as new value.
Student.update(new_dict)
print(Student)

# Set: Set is the collection of unordered items.Each element in set must be unique and immutable. 
num={1,3,4,5}
set2={1,3,2,3,2} # duplicated values are stored only once,it resolved to {1,3,2}
null_set=set() # empty set syntex.
# Boolean, int, float, string, tupple these all data type can be stored in a set but list and dict can't be stored because they mutable.
collection={} # empty dictionary
#print(type(collection))
collection=set() # empty set
print(type(collection))

# Set methods:
# 1:set.add(): adds an element.
collection.add(1)
print(collection)
collection.add("QUEST")
collection.add((23,34,"hello"))
print(collection)
# collection.add([23,90.0,"wellcome"]) #error

# 2:set.remove():remove an element.
collection.remove(1)
print(collection)

# 3:set.clear():empties the set.
print(len(collection))
#collection.clear()
#print(len(collection))

# 4:set.pop():remove a random value.
collection.pop()
print(collection)

# 5:set1.union(set2): combines both set values and return new.
set1={2,4,3,6}
set2={4,5,3,2}
print(set1.union(set2))

# 6: set1.intersection(set2): combines common values and return new.
print(set1.intersection(set2))

# Let's Practice:
# 1: Store following word meaning in python dictionary.
# table: "a piece of furniture","list of facts and figures", cat:"a small animal"
dict1={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figure"]}
print(dict1)

# 2: You are given a list of subjects for students, assume 1 class room is requared for 1 subject.how many class rooms are needed for all students?
# "Python","Java","C++","Python","JavaScript","Java","Python","Java","C++","C"
subj={"Python","Java","C++","Python","JavaScript","Java","Python","Java","C++","C"}
print("Classes needed for all the Students are:",len(subj))

#3: WAP to enter marks of subjects from user and store them in a dictionary. Start with an empty dict and add one by one,use subj as key and marks as value.
marks={}
x=int(input("enter marks of phy:"))
marks.update({"phy":x})
y=int(input("enter marks of chem:"))
marks.update({"chem":y})
z=int(input("enter marks of math:"))
marks.update({"math":z})
print(marks)

# 4: Figure out the way to store 9 and 9.0 as saperate values in the set.(you can take help of built in data type)
set={9,"9.0"}
print(set)
# OR
set={("float",9.0),("int",9)}
print(set)