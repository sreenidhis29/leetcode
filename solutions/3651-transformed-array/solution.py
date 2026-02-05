class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                steps = nums[i]
                idx = (i + steps) % n
                result[i] = nums[idx]

        return result
