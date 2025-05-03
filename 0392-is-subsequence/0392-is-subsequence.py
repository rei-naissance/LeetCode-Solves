class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        i = 0
        for char in t:
            if i == len(s):
                break
            if char == s[i]:
                i += 1    
            else:
                continue   

        return i == len(s)