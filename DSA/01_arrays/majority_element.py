"""
Algorithm: Majority Element (Brute Force)

Description:
Finds the majority element by counting the frequency of every
element and returning the one that appears more than n/2 times.

Time Complexity:
- O(n²)

Space Complexity:
- O(1)
"""
def Majority_element(arr):
    n=len(arr)
    for i in range(n):
        frequincy=0
        for j in range(0,n):
            if arr[j]==arr[i]:
                frequincy+=1
        if frequincy>n//2:
            return arr[i]   

arr=[2,1,2,1,1]
result=Majority_element(arr)
print(result)
