class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) < k or len(s) - k + 1 < need:
            return False
        
        seen = set()
        curr = 0
        mask = need - 1
        
        for i, ch in enumerate(s):
            curr = ((curr << 1) & mask) | (ch == '1')
            if i >= k - 1:
                seen.add(curr)
                if len(seen) == need:
                    return True
        
        return False
