#! usr/bin/env python3

# Time Complexity is O(N+K), where N is the length of the list
# and K is the range of numbers in the given arr
# Space is O(N+K).

from typing import List

"""

Counting sort is a sorting technique based on keys between a specific range. 
It works by counting the number of objects having distinct key values (kind of hashing). 
Then doing some arithmetic to calculate the position of each object in the output sequence.

Counting sort is a stable sort: if two items have the same key as each other, 
they should have the same relative position in the output as they did in the input.

example video: https://www.youtube.com/watch?v=7zuGmKfUt7s

Args:
        arr (List): a list that's about to be sorted if needed.
        number_of_uniElements: The unique numbers in the given arr.

        for integers we suppose all the unique elements is ranging in 10 numbers,
        from 0 to 9, and user can deciede their own "number_of_uniElements" 
        by inputing.

Return:
    None
    
"""


suppoose_all_uniElements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def counting_sort_integer(arr: List[int], number_of_uniElements: int) -> None:

    countAppear = [0] * number_of_uniElements
    res = [0] * len(arr)
    for i in arr:
        countAppear[i] += 1

    for i in range(1, len(countAppear), 1):
        countAppear[i] += countAppear[i - 1]

    for i in arr[::-1]:
        res[countAppear[i] - 1] = i
        countAppear[i] -= 1

    arr = res
    print(arr)


print("Test Case 1 is [5, 4, 3, 2, 1] with 6 unique elements and the result will be:")
counting_sort_integer([5, 4, 3, 2, 1], 6)

print("Test Case 2 is [4, 3, 1, 1, 0] with 5 unique elements and the result will be:")
counting_sort_integer([4, 3, 1, 1, 0], 5)
