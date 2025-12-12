from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))
        def cmp(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0
        arr.sort(key=cmp_to_key(cmp))
        res = "".join(arr)
        return "0" if res[0] == "0" else res
