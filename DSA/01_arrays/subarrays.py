"""
Algorithm: Print All Subarrays

Description:
Prints every possible contiguous subarray of the given array.

Time Complexity:
- O(n³)

Space Complexity:
- O(1)
"""
def print_Sub_arr(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j+1):   
                print(arr[k],end=" ")
            print()
arr=[1,2,3]
print_Sub_arr(arr)
