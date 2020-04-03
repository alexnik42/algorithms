import random

arr = []

# Open file and transform it to List
with open('file.txt', 'r') as file:
    for line in file:
        arr.append(int(line.strip()))

# Randomized QuickSort
def quick_sort(arr):

    if (not arr or len(arr) == 1): # Base case - return if length of arr < 2
        return arr

    pivot_index = random.randint(0, len(arr) - 1) # Choose random index of arr
    pivot = arr[pivot_index] # Set pivot based on random index

    arr[0], arr[pivot_index] = arr[pivot_index], arr[0] # Move pivot to the beginning of arr

    i = 1 # Set counter for pivot's position
    for j in range(i, len(arr)): # Iterate through array
        if (arr[j] < pivot): 
            arr[i], arr[j] = arr[j],arr[i] # Move element to the left part of arr
            i += 1

    arr[0], arr[i - 1] = arr[i - 1], arr[0] # Move pivot to the correct position in arr

    # Recursive calls
    if (len(arr) == 2):
        return quick_sort(arr[:1]) + quick_sort(arr[1:])
    else:
        return quick_sort(arr[:i-1]) + [pivot] + quick_sort(arr[i:])

# Run algorithm
print(quick_sort(arr))