class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        max_profit = 0
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                print(prices[right],' - ',prices[left],' makes me ',profit)
                max_profit+=profit
                left+=1
                right+=1
            else:
                left+=1
                right+=1
        
        print('Maximum profit made',max_profit)
        return max_profit