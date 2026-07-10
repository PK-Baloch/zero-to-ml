"""
Algorithm: Sum of Array Elements

Description:
Calculates the sum of all elements in an array by traversing
the array once and adding each element to a running total.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""
def calc_sum(arr):
    sum=0
    i=0
    while i<len(arr):
        sum=sum+arr[i]
        i+=1
    return sum
arr2=[2,4,6,8,10]
result=calc_sum(arr2)
print("sum of all elements of an arr is: ",result)
