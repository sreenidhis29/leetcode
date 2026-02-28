class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        bit_length = 0
        
        for num in range(1, n + 1):
            if num & (num - 1) == 0:
                bit_length += 1
            
            result = ((result << bit_length) | num) % MOD
        
        return result        
