class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        c1 = Counter(nums1)
        res = []
        for x in nums2:
            if c1[x] > 0:
                res.append(x)
                c1[x] -= 1
        return res
