"""
Algorithm: Pair Sum (Brute Force)

Description:
Checks every possible pair of elements in the array and returns
the indices of the pair whose sum equals the target value.

Time Complexity:
- O(n²)

Space Complexity:
- O(1)
"""
def Pair_arr(arr,target):
    n=len(arr)
    ans=[]
    for i in range(n):
        j=i+1
        for j in range(n):
            if(arr[i]+arr[j]==target):
                ans.append(i)
                ans.append(j)
                return ans
                

arr=[2,7,11,15]
target=int(input("enter your valid target:"))
result=Pair_arr(arr,target)
print(result) # prints index of pair sum not exact elements