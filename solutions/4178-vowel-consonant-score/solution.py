class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = c = 0
        for ch in s:
            if ch in "aeiou":
                v += 1
            elif ch.isalpha():
                c += 1
        return 0 if c == 0 else v // c
