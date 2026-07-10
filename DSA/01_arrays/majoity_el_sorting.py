"""
Algorithm: Majority Element (Sorting)

Description:
Sorts the array and counts consecutive occurrences to find
the element that appears more than n/2 times.

Time Complexity:
- O(n log n)

Space Complexity:
- O(1)
"""
def Majority_element(arr):
    arr.sort()
    n=len(arr)
    ans=arr[0]
    frequincy=1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            frequincy+=1
        else:
            frequincy=1
            ans=arr[i]
        if frequincy>=n//2:
            return ans
    return None

arr=[1,1,2,2,2,3,3,3,3,3]
result=Majority_element(arr)
print(result)