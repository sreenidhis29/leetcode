class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        w = 0
        for x in nums:
            if x != 0:
                nums[w] = x
                w += 1
        while w < len(nums):
            nums[w] = 0
            w += 1
