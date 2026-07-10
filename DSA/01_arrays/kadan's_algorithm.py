"""
Algorithm: Kadane's Algorithm

Description:
Finds the maximum sum of a contiguous subarray by maintaining
the current sum and the maximum sum while traversing the array once.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""
def Calc_Max_Sub_arr_Sum(arr):
    n=len(arr)
    Max_Sum=float('-inf')
    Current_Sum=0
    for i in range(n):
        Current_Sum+=arr[i]
        Max_Sum=max(Current_Sum,Max_Sum)
        if(Current_Sum<0):
            Current_Sum=0
    return Max_Sum

arr=[3,-4,5,4,-1,7,-8]
result=Calc_Max_Sub_arr_Sum(arr)
print(result)