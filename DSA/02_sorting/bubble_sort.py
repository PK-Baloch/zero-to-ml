# Bubble Sort

# Description:
# Sorts the array by repeatedly swapping adjacent elements if they are in the wrong order.

# Time Complexity:
# - Best Case: O(n²)      # This implementation (not optimized)
# - Average Case: O(n²)
# - Worst Case: O(n²)

# Space Complexity:
# - O(1)

def bubble_sort(nums):
  n=len(nums)
  for i in range(n):
    for j in range(0,n-i-1):
      if nums[j+1]<nums[j]:
        nums[j],nums[j+1]=nums[j+1],nums[j]
  return nums
nums=[5,3,6,4,2]
result=bubble_sort(nums)
print("After applying bubble sort algorithm sorted arr is: ",result)
