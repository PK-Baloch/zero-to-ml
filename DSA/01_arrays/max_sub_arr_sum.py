"""
Algorithm: Maximum Subarray Sum (Brute Force)

Description:
Finds the maximum sum among all possible contiguous subarrays
by checking every subarray.

Time Complexity:
- O(n²)

Space Complexity:
- O(1)
"""

def Max_subarr_Sum(arr):
    Max_Sum=float('-inf')
    n=len(arr)
    for i in range(n):
        Current_Sum=0
        for j in range(i,n):
            Current_Sum+=arr[j]
            Max_Sum=max(Current_Sum,Max_Sum)
    return Max_Sum
arr=[3,-4,5,4,-1,7,-8]
result=Max_subarr_Sum(arr)
print(result) 