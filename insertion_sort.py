#! usr/bin/env python3

# Time Complexity is O(N^2), where N is the length of the list.
# Space is O(1).

from typing import List

"""

This is a insertion sorting to sort a list
by checking one element each time and inserting to the right position.

example video: https://www.youtube.com/watch?v=OGzPmgsI-pQ

Args:
        arr (List): a list that's about to be sorted if needed.

Return:
    None
    
"""


def insertion_sort(arr: List) -> None:

    for i in range(1, len(arr), 1):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    print(arr)


testCase1 = [5, 4, 3, 2, 1]
testCase2 = [8, 2, -5, 9.5, 0, -8, 99, 6 * 9]

print("Test Case 1 is [5, 4, 3, 2, 1] and the result will be:")
insertion_sort(testCase1)

print("Test Case 2 is [8, 2, -5, 9.5, 0, -8, 99, 6*9] and the result will be:")
insertion_sort(testCase2)
