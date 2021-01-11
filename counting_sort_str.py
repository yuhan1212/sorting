#! usr/ bin/env python3

# Time Complexity is O(N^2), where N is the length of the list
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

Return:
    None
    
"""
all_str = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def counting_sort_str(arr: List[str]) -> None:

    countAppear = [0] * 26
    res = [0] * len(arr)

    for a in arr:
        position = all_str.index(a)
        countAppear[position] += 1

    for i in range(1, len(countAppear), 1):
        countAppear[i] += countAppear[i - 1]

    for a in arr[::-1]:
        position = all_str.index(a)
        res[countAppear[position] - 1] = a
        countAppear[position] -= 1

    arr = res
    print(arr)


print("Test Case 1 is [d, r, f, s, r, a] and the result will be:")
counting_sort_str(["d", "r", "f", "s", "r", "a"])

print("Test Case 2 is [a, a, w, b, c, w, f] and the result will be:")
counting_sort_str(["a", "a", "w", "b", "c", "w", "f"])
