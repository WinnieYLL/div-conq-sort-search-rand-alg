# array = np.loadtxt("QuickSort.txt")
# quicksort(array)

# 162085
# 164123

import numpy as np

def quicksort(array):
    return quicksort_helper(array, 0, np.size(array))

def quicksort_helper(array, left, right):
    # Sorts the array from index left inclusive to index right not inclusive
    
    # base case
    if right <= left:
        return 0
    
    #mid, num_comp_part = partition_first(array, left, right)
    #mid, num_comp_part = partition_last(array, left, right)
    mid, num_comp_part = partition_median_of_three(array, left, right)
    num_comp_left = quicksort_helper(array, left, mid)
    num_comp_right = quicksort_helper(array, mid+1, right)
    
    return num_comp_part + num_comp_left + num_comp_right

def partition_first(array, left, right):
    # split array from left index inclusive to right index not inclusive into two parts
    
    # Always use first element as pivot
    pivot = array[left]
    
    i = left + 1
    
    num_comp = 0
    
    for j in range(i, right):
        # if array[j] >= pivot, nothing to do
        num_comp += 1
        
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
            
    swap(array, left, i-1)
    
    return i-1, num_comp
    
def partition_last(array, left, right):
    # split array from left index inclusive to right index not inclusive into two parts
    
    # Always use last element as pivot
    swap(array, left, right-1)
    
    return partition_first(array,left,right)

def partition_median_of_three(array, left, right):
    # split array from left index inclusive to right index not inclusive into two parts
    
    # median of three variant
    middle = int(np.floor((left+right-1)/2))
    med = np.median(array[[left, middle, right-1]])
    
    if med == array[middle]:
        swap(array, left, middle)
    
    if med == array[right-1]:
        swap(array, left, right-1)
    
    return partition_first(array,left,right)
            
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp