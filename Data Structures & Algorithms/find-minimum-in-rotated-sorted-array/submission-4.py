class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        min_check = nums[0]
        for item in nums_set:
            if (item-1) not in nums_set:
                if min_check > item:
                    min_check = item
                
        
        return min_check