class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        maxlen = max((len(w) for w in wordDict), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            start = max(0, i - maxlen)
            for j in range(start, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]
