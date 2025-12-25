class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        ans = 0
        dec = 0
        for i in range(k):
            val = happiness[i] - dec
            if val <= 0:
                break
            ans += val
            dec += 1
        return ans
