class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        def four_div_sum(x):
            divs = set()
            for d in range(1, int(math.isqrt(x)) + 1):
                if x % d == 0:
                    divs.add(d)
                    divs.add(x // d)
                    if len(divs) > 4:
                        return 0
            return sum(divs) if len(divs) == 4 else 0

        total = 0
        for num in nums:
            total += four_div_sum(num)
        return total
