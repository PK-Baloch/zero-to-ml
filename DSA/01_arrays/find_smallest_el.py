# smallest number in arr.

# Description:
# Finds and returns the smallest element in an array by comparing
# each element with the current smallest value.

# Time Complexity:
# - Best Case: O(n)
# - Average Case: O(n)
# - Worst Case: O(n)

# Space Complexity:
# - O(1)

def smallest_el(arr):
    if not arr:
        return None
    smallest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
    return smallest
arr = [-1,22,1,-10]
result=smallest_el(arr)
if result is None:
    print("You provide an empty list")
else:
    print("Smallest no: in arr is: ",result)
