class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        left, right = 0, len(heights) - 1

        max_value, max_water = 0, 1

        while left < right:
            max_water = (min(heights[left], heights[right])*(abs(right-left)))
            max_value = max(max_value, max_water)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_value