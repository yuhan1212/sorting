#!/usr/bin/env python3

# Time complexity is O(N logN), where N is the length of the list.
# Space is O(N) because it requires additional memory space 
# to store the auxiliary arrays.

from typing import List

"""

Like QuickSort, Merge Sort is a Divide and Conquer algorithm. 
It divides the input array into two halves, calls itself for the two halves, 
and then merges the two sorted halves. 

example video: https://www.youtube.com/watch?v=JSceec-wEyw

Args:
        arr (List): a list that's about to be sorted if needed.

Return:
    None
    
"""


def merge_sort(arr: List[int]) -> None:

    if len(arr) > 1:

        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        merge_sort(left_arr)
        merge_sort(right_arr)

        a = l = r = 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[a] = left_arr[l]
                l += 1
                a += 1
            else:
                arr[a] = right_arr[r]
                r += 1
                a += 1

        arr[a:] = left_arr[l:] or right_arr[r:]


test1 = [4, 5, 6, 10, 1, 2, 3]
merge_sort(test1)
print("Test Case 1 is [4, 5, 6, 10, 1, 2, 3] and the merge sort result is:")
print(test1)

test2 = [5, 6, 4, 3, 2, 1, 0]
merge_sort(test2)
print("Test Case 1 is [5, 6, 4, 3, 2, 1, 0] and the merge sort result is:")
print(test2)
