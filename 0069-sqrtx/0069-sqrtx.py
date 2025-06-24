class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(x):
            if i ** 2 > x:
                return i - 1
            if i ** 2 == x:
                return i
            if x == 2:
                return 1

        return x