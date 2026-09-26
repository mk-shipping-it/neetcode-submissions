class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # flatten array
        
        # one and zeroes check
        if n == 1:
            return x

        if n == 0:
            return 1
        
        # capped at -1
        if n == -1:
            return 1/x
        

        # even odd check
        elif n % 2 == 0:
            return self.myPow(x * x, n//2)
        elif n % 2 != 0:
            return x * self.myPow(x * x, n//2)