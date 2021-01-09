#!/usr/bin/env python3

# The worst and average time complexity is O(N^2), where N is the length of the list.
# The best time complexity is O(N), where N is the length of the already sorted list.
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
    no_swap_happen: bool = True

    # Bubble sort
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):

            if arr[i] > arr[i + 1]:
                no_swap_happen = False
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

            if j == 0 and i == len(arr) - 2 and no_swap_happen is True:
                print("We hit the best case with O(N)")
                print("arr: ", arr)
                return

    print("arr: " + str(arr))


bubble_sort(arr)


bubble_sort([1, 2, 3])
