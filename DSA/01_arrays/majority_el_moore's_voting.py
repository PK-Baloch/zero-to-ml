"""
Algorithm: Moore's Voting Algorithm

Description:
Finds the majority element by maintaining a candidate and a counter.
The majority element is guaranteed to remain as the final candidate
if it appears more than n/2 times.

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""
def Majority_element(arr):
    n=len(arr)
    freq=0
    ans=0
    for i in range(n):
        if(freq==0):
            ans=arr[i]
        if(arr[i]==ans):
            freq+=1
        else:
            freq-=1
    if arr.count(ans)>n//2:
        return ans
    else:
        return None

arr=[2,1,2,3,2,]
result=Majority_element(arr)
print(result)
