class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        white = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                white += 1
                continue
            else:
                swaps += white

        return swaps    