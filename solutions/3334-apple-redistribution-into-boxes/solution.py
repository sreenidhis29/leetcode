class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        curr = 0
        for i, cap in enumerate(capacity):
            curr += cap
            if curr >= total_apples:
                return i + 1
