class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        def expand_around_center(left: int, right: int) -> int:
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count
            
        for i in range(n):
            count += expand_around_center(i, i)
            count += expand_around_center(i, i + 1)
            
        return count
