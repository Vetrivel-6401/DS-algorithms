# Selection Sort
# --------------
# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

'''To implement the Selection Sort algorithm in a programming language, we need:

1.An array with values to sort.
2.An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. 
This loop must loop through one less value each time it runs.
3.An outer loop that controls how many times the inner loop must run. For an array with n
 values, this outer loop must run n-1 times'''


#-------------------sample one -----------------
def selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        
        min_value=arr.pop(min_index)
        arr.insert(i,min_value)
    print(arr)


arr=[2,3,4,1,7,5,6,9,8]
selection_sort(arr)

'''The above code has a shifing problem...The solution swapping values'''

#-------------sample two --------------

def new_selection_sort(my_array):
    n=len(my_array)

    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if my_array[j]<my_array[min_index]:
                min_index=j
        my_array[i],my_array[min_index]=my_array[min_index],my_array[i]

    print(my_array)


my_array=[100,99,55,44,22,31,1]
new_selection_sort(my_array)