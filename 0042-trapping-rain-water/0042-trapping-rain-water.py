class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        total = 0

        leftMax, rightMax = 0, 0
        while i < j:
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])
            
            if height[i] < height[j]:
                total += leftMax - height[i]
                i += 1
            else:
                total += rightMax - height[j]
                j -= 1

        return total
            
