"""
Algorithm: Reverse Array

Description:
Reverses an array by swapping the first and last elements,
then moving towards the center until the array is completely reversed.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

Space Complexity:
- O(1)
"""
def Reverse_arr(arr):
    start=0
    end=len(arr)-1
    i=0
    while i<len(arr)//2:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
        i+=1
    return arr
arr1=[33,23,63,53,43,23]
print("arr before swaping : ",arr1)
result=Reverse_arr(arr1)
print("arr after swaping : ",result)
