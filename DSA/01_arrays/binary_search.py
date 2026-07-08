# binary search
def binary_search(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(target<arr[mid]):
         end=mid-1
        elif(target>arr[mid]):
         start=mid+1
        else:
         return mid
    return -1
arr=[2,4,6,8,10,12,14]
target=int(input("enter your target: "))
result=binary_search(arr,target)
if result!=-1:
  print("target is found at indx: ",result)
else:
  print("target is not found")
