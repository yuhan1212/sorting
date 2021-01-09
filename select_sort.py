#!/usr/bin/env python3

# Time Complexity is O(N^2), where N is the length of the arr.
# Space is O(1).

from typing import List

arr = [5, 3, 8, 1, 9, 6]


def select_sort(arr: List) -> None:
    """
    This is a select sorting to sort a list
    by selecting the smaller element closer to the front.

    example video: https://www.youtube.com/watch?v=xWBP4lzkoyM

    Args:
        arr (List): a list that's about to be sorted if needed.

    Return:
        None
    """

    # for O(N) best case
    is_arr_sorted: bool = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_arr_sorted = False
            break

    if is_arr_sorted:
        print("We hit the best case with O(N)")
        print("arr: ", arr)
        return

    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr), 1):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp

    print("arr is ", arr)


select_sort(arr)
select_sort([1, 5, 7, 0, -1, 88888, 0.8])
