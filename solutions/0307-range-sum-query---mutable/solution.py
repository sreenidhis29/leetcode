class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]        
        self.bit = [0] * (self.n + 1)
        for i, v in enumerate(nums):
            self._add(i + 1, v)

    def _add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def sumRange(self, left, right):
        return self._sum(right + 1) - self._sum(left)
