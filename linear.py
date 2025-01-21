def linear_serach(arr,target):
    
    size=len(arr)

    for i in range(size):
        if arr[i]==target:
            return i
    return -1



arr=[3,5,11,13,17,88,19]
target=13

result=linear_serach

if result !=-1:
    print('value',target,'fount at index: ',result)
else:
    print('Target not found in the array')
