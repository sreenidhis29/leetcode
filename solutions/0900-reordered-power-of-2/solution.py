class Solution(object):
    def reorderedPowerOf2(self, n):
        from collections import Counter

        def digit_count(x):
            return Counter(str(x))

        target = digit_count(n)

        for i in range(31):  # 2^0 to 2^30
            if digit_count(1 << i) == target:
                return True

        return False

