from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        for char in ransom_count:
            if ransom_count[char] > magazine_count.get(char, 0):
                return False
        return True

