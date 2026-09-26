import math
class Solution:
    def isHappy(self, n: int) -> bool:
        
        result = set()
        
        while n not in result:
            result.add(n)
            n = self.sumDo(n)
            print(result)
        if n == 1:
            return True
        
        return False
        
    def sumDo(self, m):
        if m == 1:
            return 1
        elif m == 0:
            return 0
        else:
            return pow(m%10, 2) + self.sumDo(m//10)
