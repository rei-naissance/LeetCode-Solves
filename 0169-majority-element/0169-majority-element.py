"""
3 2 3

2 2 1 1 1 2 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return_map = {}
        
        for i in range(len(nums)):
            if nums[i] in return_map:
                return_map[nums[i]] += 1
            if nums[i] not in return_map:
                return_map[nums[i]] = 1

        print(return_map)

        return max(return_map, key=return_map.get)
