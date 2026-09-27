class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g - children

        left, right = 0, 0
        count = 0

        g.sort()
        s.sort()

        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                left+=1
                #right+=1
                count+=1
            right+=1

            # right only moves when the greedy kid is fed
            # left moves naturally, kids that have a greed score higher than 
        return left