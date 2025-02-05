def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        insert_index=i
        min_value=arr.pop(i)

        for j in range(i-1,-1,-1):
            if arr[j]>min_value:
                insert_index=j

        arr.insert(insert_index,min_value)

arr=[100,23,42,23,1,2,3,4,66]
insertion_sort(arr)
print(arr)


#--------------shifting problem--------------------

def insertion_sort_new(my_arr):
    n=len(my_arr)

    for i in range(1,n):
        insert_inbdex=i
        min_value=my_arr[i]

        for j in range(i-1,-1,-1):
            if my_arr[j]>min_value:
                my_arr[j+1]=my_arr[j]
                insert_inbdex=j
            else:
                break
        my_arr[insert_inbdex]=min_value

arr=[103,23,43,23,1,2,3,44,66]
insertion_sort_new(arr)
print(arr)