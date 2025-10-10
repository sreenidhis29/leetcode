from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_count = Counter(words)
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        n = len(s)
        indices = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word not in word_count:
                    current_count.clear()
                    count = 0
                    left = right
                    continue

                current_count[word] += 1
                count += 1

                while current_count[word] > word_count[word]:
                    removed = s[left:left + word_len]
                    current_count[removed] -= 1
                    count -= 1
                    left += word_len

                if count == total_words:
                    indices.append(left)

        return indices
