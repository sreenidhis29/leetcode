class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # For one row:
        # type1: 3 colors all different (ABC) -> 6 ways
        # type2: two colors same, one different (ABA) -> 6 ways
        diff = 6
        same = 6

        for _ in range(2, n + 1):
            new_diff = (2 * diff + 2 * same) % MOD
            new_same = (2 * diff + 3 * same) % MOD
            diff, same = new_diff, new_same

        return (diff + same) % MOD
