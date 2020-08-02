# array_in = np.loadtxt("IntegerArray.txt")
# array_out, icount = mergesort(array_in)
# icount

import numpy as np

def mergesort(array):
    length = np.size(array)
    
    if length <= 1:
        return array, 0
    
    middle = int(np.ceil(length/2))
    
    
    array_left, lcount = mergesort(array[0:middle])
    array_right, rcount = mergesort(array[middle:length])
    array, scount = merge(array_left, array_right)
    
    return array, lcount+rcount+scount
    
    
def merge(array_left, array_right):
    array = np.array([])
    
    left = 0
    right = 0
    icount = 0
    
    left_size = np.size(array_left)
    right_size = np.size(array_right)
    while (left < left_size) & (right < right_size):
        if array_left[left] <= array_right[right]:
            array = np.append(array, array_left[left])
            left = left + 1
        else:
            array = np.append(array, array_right[right])
            right = right + 1
            icount = icount + left_size - left

    for i in range(left, left_size):
        array = np.append(array, array_left[i])
        
    for i in range(right, right_size):
        array = np.append(array, array_right[i])    
        
    return array, icount