class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # a lot of slicing going on lately

        
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]

        
        # apparently you can copy back to array
        # create a shallow copy, perhaps? Credits : Tianrui Zhang

        nums1[:] = nums1[:m]
        print(nums1)
        
        # easy pointer approach
        left, right = 0, 0
        while left < len(nums1) and right < n:
            if nums1[left] > nums2[right]:
                nums1.insert(left, nums2[right])
                right+=1
            left+=1
        nums1.extend(nums2[right:])
        print(nums1)