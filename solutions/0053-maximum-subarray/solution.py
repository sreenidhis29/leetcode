class Solution:
    def maxSubArray(self, nums):
        best = cur = nums[0]
        for x in nums[1:]:
            if cur < 0:
                cur = x
            else:
                cur += x
            if cur > best:
                best = cur
        return best
