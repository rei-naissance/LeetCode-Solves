class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                ret += char

        ret = ret.lower()
        print(ret)

        flag = ret == ret[::-1]

        return flag