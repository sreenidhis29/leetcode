class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # Step 1: Build powers array from binary representation
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        powers.sort()

        # Step 2: Build prefix product array
        prefix = [1] * len(powers)
        prefix[0] = powers[0] % MOD
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i - 1] * powers[i]) % MOD

        # Step 3: Answer each query
        answers = []
        for left, right in queries:
            if left == 0:
                answers.append(prefix[right])
            else:
                inv = pow(prefix[left - 1], MOD - 2, MOD)
                answers.append((prefix[right] * inv) % MOD)

        return answers
