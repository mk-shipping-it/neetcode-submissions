class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ar = []
        for num in nums1:
            if num in nums2:
                ar.append(num)
        
        for num in nums2:
            if num in nums1:
                ar.append(num)

        return list(set(ar))