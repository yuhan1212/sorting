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


Args:
        arr (List): a list that's about to be sorted if needed.
        While calculating the range of unique numbers in the given arr,
        we find the max and min numbers, and set min index as 0,
        to keep the relative position.
        In this case, we do not need to ask the range as input.

Return:
    None
    
"""

def counting_sort_any_int(arr: List[int]) -> None:

    max_number = max(arr)
    min_number = min(arr)

    res = [0]*len(arr)
    count = [0]*(max_number - min_number + 1)

    for i in arr:
        count[i - min_number] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in arr[::-1]:
        res[count[i - min_number] - 1] = i
        count[i - min_number] -= 1

    arr = res
    print(arr)

print("Test Case 1 is [2, 5, -1, 4, 0, 99, 2, -5, 18] and the result will be:")
counting_sort_any_int([2, 5, -1, 4, 0, 99, 2, -5, 18])

print("Test Case 2 is [-4, -3, -1, -1, 20] and the result will be:")
counting_sort_any_int([-4, -3, -1, -1, 20])

    