#! usr/bin/env python3

# The worst and average time complexity is O(N^2),
# where N is the length of the list and pivot is the max or min in the list.
# The best time complexity is O(N log(N)).
# Space is O(log(N)) as we use recursion.

from typing import List

"""

Quick sort is a highly efficient sorting algorithm and is based on 
partitioning of array of data into smaller arrays. 
A large array is partitioned into two arrays one of which 
holds values smaller than the specified value, say pivot, 
based on which the partition is made and another array 
holds values greater than the pivot value.

example video: https://www.youtube.com/watch?v=uXBnyYuwPe8&t=1153s

Args:
        arr (List): a list that's about to be sorted if needed.

Return:
    None
    
"""


def quick_sort(arr: List[int]) -> List:

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    pivot = arr[-1]
    i = 0  # pointer_smaller_part
    j = len(arr) - 2  # pointer_bigger_part
    while i <= j:
        if arr[i] > pivot and arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < pivot and arr[j] < pivot:
            i += 1
        elif arr[i] > pivot and arr[j] > pivot:
            j -= 1
        elif i == j:
            if arr[i] < pivot:
                i += 1

    smaller = arr[:i]
    bigger = arr[i:-1]

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


print("Test Case 1 is [4, 5, 6, 10, 1, 2, 3] and the quick sort result is:")
print(quick_sort([4, 5, 6, 10, 1, 2, 3]))

print("Test Case 2 is [5, 4, 3, 2, 1, 99] and the quick sort result is:")
print(quick_sort([5, 4, 3, 2, 1, 99]))
