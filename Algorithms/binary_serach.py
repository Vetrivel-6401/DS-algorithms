# Binary Search Implementation
# To implement the Binary Search algorithm we need:

# An array with values to search through.
# A target value to search for.
# A loop that runs as long as left index is less than, or equal to, the right index.
# An if-statement that compares the middle value with the target value, and returns the index if the target value is found.
# An if-statement that checks if the target value is less than, or larger than, the middle value, and updates the "left" or "right" variables to narrow down the search area.
# After the loop, return -1, because at this point we know the target value has not been found.

def binary_serach(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right=mid-1
    return -1    
    



arr=[1,3,4,6,7,18,22,23,24,32]
target=18
result=binary_serach(arr,target)
if result !=-1:
    print('Target found at index: ',result)
else:
    print("Target Not found in the array")

