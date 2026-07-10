"""
Algorithm: Print Unique Elements

Description:
Finds and prints all elements that appear exactly once in the array
by checking the frequency of each element.

Time Complexity:
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

Space Complexity:
- O(n)
"""
arr=[2,3,1,5,2,6,1,4] 
unique_arr=[]
for i in arr:
    if arr.count(i)==1:
        unique_arr.append(i)

print("unique values of arr are: ",unique_arr)
