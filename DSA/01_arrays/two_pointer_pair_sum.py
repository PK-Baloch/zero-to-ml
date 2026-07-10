"""
Algorithm: Pair Sum (Two Pointer)

Description:
Finds the pair whose sum equals the target using two pointers.
This algorithm works only on a sorted array.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""
def Pair_Sum(arr,target):
    i=0
    j=len(arr)-1
    ans=[]
    while(i<j):
        PS=arr[i]+arr[j]
        if(target<PS):
            j-=1
        elif(target>PS):
            i+=1
        else:
            ans.append(i)
            ans.append(j)
            return ans
arr=[2,7,11,15]
target=int(input("enter a valid target:"))
result=Pair_Sum(arr,target)
print(result)