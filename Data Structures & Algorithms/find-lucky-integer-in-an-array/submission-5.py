from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for item in arr:
            
            if item == arr.count(item):
                freq[item] = arr.count(item)
                print(f'Item {item} has a frequency of {arr.count(item)} in the array')
                res = max(res, item)
                print(res)
        
        return -1 if res < 1 else res
        