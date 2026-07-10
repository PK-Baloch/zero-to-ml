"""
Algorithm: Intersection of Two Arrays

Description:
Finds the common elements between two arrays by comparing every
element of the first array with every element of the second array.

Time Complexity:
- Best Case: O(n * m)
- Average Case: O(n * m)
- Worst Case: O(n * m)

Space Complexity:
- O(min(n, m))
"""
arr1=[2,3,5,6,1,4] 
arr2=[2,0,9,5,8,3]

shared_arr=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            shared_arr.append(arr1[i])
print(shared_arr)
