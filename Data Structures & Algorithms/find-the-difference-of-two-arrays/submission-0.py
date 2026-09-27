class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # items in set 1 but not in set 2

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = [[], []]
        for item in nums1_set:
            if item not in nums2_set:
                res[0].append(item)
                print(item, end=" ")
                # append and not extend to prevent flattening the result
        
        count = 0
        for item in nums2_set:
            if item not in nums1_set:
                res[1].append(item)
                print(item, end=" ")
                # append and not extend to prevent flattening the result
        
        print(f'\nResult set: {res}')
        return res