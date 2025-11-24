class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for b in nums:
            cur = ((cur << 1) + b) % 5
            res.append(cur == 0)
        return res
