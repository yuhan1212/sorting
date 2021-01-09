#!/usr/bin/env python3

# The worst and average time complexity is O(N^2), where N is the length of the list.
# The best time complexity is O(N), where N is the length of the already sorted list.
# Space is O(1).

from typing import List


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

    # Bubble sort
    for j in range(len(arr) - 1):
        no_swap_happen: bool = True

        for i in range(len(arr) - j - 1):

            if arr[i] > arr[i + 1]:
                no_swap_happen = False
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

        if no_swap_happen is True:
            print("No further sorting is needed, exiting bubble_sort")
            print(arr)
            return

    print(arr)


testBestCase = [1, 2, 3, 4, 5]
testWorstCase = [5, 4, 3, 2, 1]
print("Best Case is [1, 2, 3, 4, 5] and the result will be:")
bubble_sort(testBestCase)

print("Worst Case is [5, 4, 3, 2, 1] and the result will be:")
bubble_sort(testWorstCase)
