#Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr



arr=[11,13,2,1,44,55,33,22,5,7]
sorted_array=bubble_sort(arr)
print(sorted_array)