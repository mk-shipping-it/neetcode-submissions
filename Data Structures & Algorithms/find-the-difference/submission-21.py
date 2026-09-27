class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sum_t = 0
        for item in t:
            print(f'{item} is represented in ASCII as {ord(item) - ord('a')}')
            sum_t+=ord(item) - ord('a')
        
        sum_s = 0
        for item in s:
            print(f'{item} is represented in ASCII as {ord(item) - ord('a')}')
            sum_s+=ord(item) - ord('a')
        
        diff = chr((sum_t - sum_s) + ord('a'))
        print(f'Difference: {chr((sum_t - sum_s) + ord('a'))}')
        
        return diff