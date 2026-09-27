from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        map_tracker = defaultdict(int)
        map_set = set() # empty set
        max_window = 0
        l = 0

        for item in range(len(s)):
            while s[item] in map_set:
                map_set.remove(s[l])
                l+=1
            map_set.add(s[item])
            max_window = max(max_window, item-l+1)

        return max_window