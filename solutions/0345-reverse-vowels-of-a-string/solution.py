class Solution:
    def reverseVowels(self, s: str) -> str:
        s_l = list(s)
        l = 0
        r = len(s) - 1

        vowels = set("aeiouAEIOU")

        while l < r:
            while l < r and s_l[l] not in vowels:
                l += 1
            while l < r and s_l[r] not in vowels:
                r -= 1

            if l < r:
                s_l[l], s_l[r] = s_l[r], s_l[l]
                l += 1
                r -= 1
        return "".join(s_l)

        
                            
