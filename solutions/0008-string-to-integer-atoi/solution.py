class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] in ['-', '+']:
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
