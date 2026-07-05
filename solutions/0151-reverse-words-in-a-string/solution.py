class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split()
        res = []
        for i in range(len(s_l) - 1, - 1, -1):
            res.append(s_l[i])
            if i != 0:
                res.append(" ")
        return "".join(res)
