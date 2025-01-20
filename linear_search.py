def linear_search(arr,target):
    n=len(arr)

    for i in range(n):
        if arr[i]==target:
            return i
    return -1

arr=[2,3,4,6,78,200,356]
target=78

result=linear_search(arr,target)

if result !=-1:
    print('Target',target,'fount at index :',result)
else:
    print('Target not found in the array')