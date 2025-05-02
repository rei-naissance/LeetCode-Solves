class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        # flag = False
        # ctr = 0

        # for i in range(len(s) - 1, -1, -1):
        #     if s[i].isalpha() == True:
        #         flag = True
        #     if s[i] == ' ' and flag:
        #         break
        #     elif s[i] == ' ' and not flag: 
        #         continue
        #     else:
        #         ctr += 1

        # return ctr

        return len(s.strip().split()[-1])