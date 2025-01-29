# To implement the Bubble Sort algorithm in a programming language, we need:

# An array with values to sort.
# An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.


def bubble_sort(arr):
    size=len(arr)

    for i in range(size-1):
        swap=False
        for j in range(size-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=True
        if not swap:
            break



arr=[4,3,5,6,7,8,18,99,112,34,55,23]
bubble_sort(arr)
print(arr)