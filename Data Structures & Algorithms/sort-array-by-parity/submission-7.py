class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        # same movement style problems

        
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums
            

        # flexible to apply this in problems that require moving elements to the front