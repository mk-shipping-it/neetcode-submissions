class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # sentinel value
        nums.append(0)
        maxVal = 0
        index_0 = -1
        
        while 0 in nums:
            index_0 = nums.index(0)
            print(f'What the array look like without the first 0 {nums[:index_0]}')
            # slice
            maxVal = max(maxVal, len(nums[:index_0]))
            nums = nums[index_0+1:]
        
        return maxVal