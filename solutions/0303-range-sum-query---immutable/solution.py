class NumArray:
    def __init__(self, nums):
        self.pref = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.pref[i + 1] = self.pref[i] + v
    def sumRange(self, left, right):
        return self.pref[right + 1] - self.pref[left]
