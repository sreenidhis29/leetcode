class Solution:
    def minOperations(self, s: str) -> int:
        mismatch0 = 0
        mismatch1 = 0
        
        for i, ch in enumerate(s):
            if ch != ('0' if i % 2 == 0 else '1'):
                mismatch0 += 1
            if ch != ('1' if i % 2 == 0 else '0'):
                mismatch1 += 1
        
        return min(mismatch0, mismatch1)
