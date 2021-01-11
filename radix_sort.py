#! usr/bin/env python3

# Time Complexity is O(NK), where N is the length of the list
# and K is the range of numbers in the given arr
# Space is O(N+K).

from typing import List

"""

Radix sort is based on counting sort.
It avoids comparison by creating and distributing elements into buckets 
according to their radix. Then doing some arithmetic as counting sort.

example video: https://www.youtube.com/watch?v=nu4gDuFabIM

Args:
        arr (List): a list that's about to be sorted if needed.

Return:
    None
    
"""


def radix_sort(arr: List[int]) -> None:
    max_number = max(arr)

    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = [0] * len(arr)
    divider = 10

    while max_number > 0:

        count = [0] * 10
        res = [0] * len(arr)

        for a in arr:
            count[(a % divider // (divider // 10))] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for a in arr[::-1]:
            res[count[(a % divider // (divider // 10))] - 1] = a
            count[(a % divider // (divider // 10))] -= 1

        arr = res
        divider *= 10
        max_number //= 10

    print(arr)


print("Test Case 1 is [1, 10, 100, 1000] after radix sort:")
radix_sort([1, 10, 100, 1000])

print("Test Case 2 is [9, 20, 1039,3162, 338, 282, 762, 62] after radix sort:")
radix_sort([9, 20, 1039, 3162, 338, 282, 762, 62])
