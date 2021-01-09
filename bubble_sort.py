#!/usr/bin/env python3

# Time Complexity is O(N^2), where N is the len(arr).
# Space is O(1).

from typing import List


arr = [1, 5, 7, 0, -1, 88888, 0.8]


def bubble_sort(arr: List) -> None:
    """
    This is a bubble sorting to sort a list
    by bubbling up the larger element closer to the end.

    example video: https://www.youtube.com/watch?v=nmhjrI-aW5o

    Args:
        arr (List): a list that's about to be sorted if needed.

    Return:
        None
    """

    # For the O(N) best case
    is_arr_sorted: bool = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_arr_sorted = False
            break

    if is_arr_sorted:
        print("We hit the best case with O(N)")
        print("arr: ", arr)
        return

    # Bubble sort
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    print("arr: " + str(arr))


bubble_sort(arr)


bubble_sort([1, 2, 3])
