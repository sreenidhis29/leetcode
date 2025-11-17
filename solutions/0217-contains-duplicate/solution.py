class Solution:
    def containsDuplicate(self, nums):
        s = set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False
