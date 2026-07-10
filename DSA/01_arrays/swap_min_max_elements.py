"""
Algorithm: Swap Minimum and Maximum Element

Description:
Finds the minimum and maximum elements in an array along with their
indices, then swaps their positions. Returns the modified array.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""
def swap(arr):
    if not arr:
        return None
    min_no=arr[0]
    min_indx=0
    max_no=arr[0]
    max_indx=0
    for i in range(len(arr)):
        if arr[i]<min_no:
            min_no=arr[i]
            min_indx=i

        if arr[i]>max_no:
            max_no=arr[i]
            max_indx=i
    arr[min_indx],arr[max_indx]=max_no,min_no
    return arr


arr1=[1,3,5,7,9]
print("arr before swaping min and max elements: ",arr1)
result=swap(arr1)
print("arr after swaping min and max elements: ",result)
