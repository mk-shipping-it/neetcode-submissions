class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        right = len(nums) - 1

        if not nums:
            return 0
        if val not in nums:
            return len(nums)

        while val in nums:
            index_val = nums.index(val)

            # get the occurence then swap
            nums[index_val], nums[right] = nums[right], nums[index_val]
            print(nums)
            # once swapped either reduce the array or modify so that the next index of val stands

            # new position of val -> end of the array
            nums[right] = '_'
            print(nums)
            right = right - 1

        # basic splice
        return len(nums[:nums.index('_')])