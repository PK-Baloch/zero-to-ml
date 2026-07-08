#Linear Search:

# Description:
# Searches for the target element by checking each element one by one.

# Time Complexity:
# - Best Case: O(1)
# - Average Case: O(n)
# - Worst Case: O(n)

# Space Complexity:
# - O(1)

def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1

numbers=[23,55,65,78,98,10]
target=int(input("enter the number you want to search:"))
result=linear_search(numbers,target)
if result != -1:
    print("Number found at index",result)
else:
    print("Number not found.")
