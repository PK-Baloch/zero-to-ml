"""
Algorithm: Find Second Largest Element

Description:
Finds and returns the second largest distinct element in an array by
maintaining the largest and second largest values while traversing the
array only once. Returns None if the array has fewer than two elements
or if no second largest distinct element exists.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""
def second_largest_no(arr):
    n=len(arr)
    if n<2:
        return None
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(n):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]>second_largest and arr[i]!=largest:
            second_largest=arr[i]
    if second_largest==float('-inf'):
        return None
    return second_largest
arr=[10,1,1,-2]
result=second_largest_no(arr)
print(result)
