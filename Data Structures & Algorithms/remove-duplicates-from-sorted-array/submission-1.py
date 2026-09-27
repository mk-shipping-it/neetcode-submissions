class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, right = 0, 1
        nums[:] = nums + list('_')

        while right < len(nums):
            if nums[right] == nums[left]:
                print(nums[right],'_')
                right+=1
                if nums[right] == '_':
                    nums[:] = nums[:left+1] + nums[right:]

            else:
                print(f'right pointer at number thats mismatched. The number {nums[right]}; right pointer {right}')
                
                print(f'first half {nums[:left+1]}')
                print(f'second half {nums[right:]}')
                nums[:] = nums[:left+1] + nums[right:]
                print(f'\n Nums now: {nums}')
                left+=1
                right=left+1
                print(f'Left pointer at {left} while right pointer at {right}')
        
        
        nums[:] = nums[:-1]
        return len(nums)