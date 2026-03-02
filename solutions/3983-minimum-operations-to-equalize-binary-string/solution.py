class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zero = 0
        slen = len(s)
        zero = s.count('0')

        if not zero:
            return 0

        if slen == k:
            return 1 if zero == slen else -1
        if not k&1 and zero&1:
            return -1

        base = slen - k

        if not zero & 1:
            even = math.ceil(zero/min(k,base))
            even += even & 1
            if not k&1:
                odd = max(math.ceil(zero / k), math.ceil((slen - zero) / base))
                odd += (odd & 1)^1
                return min(odd, even)
            else:
                return even
        else:
            odd = max(math.ceil(zero / k), math.ceil((slen - zero) / base))
            odd += (odd & 1)^1
            return odd
