class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # sometimes its best to visit other options
        # this problem can be solved by a min() and a second_min()


        # problem requires finding out possible combinations so do two pointers stand a chance?


        min1 = float('inf')
        min2 = float('inf')
        
        for price in prices:
            
            if price < min1:
                min1, min2 = price, min1
                #min2 = min1
            elif min2 > price:
                min2 = price
            
        print(min1)
        
        print(min2)

        leftover = money - (min1 + min2)
        return money if leftover < 0 else leftover

        