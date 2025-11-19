class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(x):
            s = 0
            while x:
                s += (x % 10) ** 2
                x //= 10
            return s
        slow = n
        fast = nxt(n)
        while fast != 1 and slow != fast:
            slow = nxt(slow)
            fast = nxt(nxt(fast))
        return fast == 1
