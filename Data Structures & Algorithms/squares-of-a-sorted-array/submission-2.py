class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # shows you dont need one array to solve a two pointer problem
        # similar in taste to the container with most water problem
        
        # mostly when the array is sorted try an recall container with most water 
        # <= when the middle item needa be considered

        result = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result.append(nums[left] * nums[left])
                left+=1
            else:
                result.append(nums[right] * nums[right])
                right-=1

        
        # instead of reversing the result array you could fill the elements from the rear
        return result[::-1]