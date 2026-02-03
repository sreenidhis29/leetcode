class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n =  len(nums)
        i = 0

        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        p = i

        while i < n -1 and nums[i] > nums[i + 1]:
            i += 1
        if i == p or i == n - 1:
            return False
        q = i

        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
