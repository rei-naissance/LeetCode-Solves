class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
        # idx = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[idx] = nums[i]
        #         print(nums)
        #         idx += 1
        
        # for i in range(idx, len(nums)):
        #     nums[i] = 0

        """
            0 1 0 3 12
            1 1 0 3 12
            1 3 0 3 12
            1 3 12 3 12
            1 3 12 0 12
            1 3 12 0 0
        """