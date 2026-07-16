class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        step_s, step_t = 0, 0
        while i >= 0 or j >= 0:
            #Iterate for s
            while i >= 0:
                if s[i] == "#":
                    step_s += 1
                    i -= 1
                elif step_s > 0:
                    step_s -= 1
                    i -= 1
                else:
                    break
            #Iterate for t
            while j >= 0:
                if t[j] == "#":
                    step_t += 1
                    j -= 1
                elif step_t > 0:
                    step_t -= 1
                    j -= 1
                else:
                    break
            #Comparison
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True       
