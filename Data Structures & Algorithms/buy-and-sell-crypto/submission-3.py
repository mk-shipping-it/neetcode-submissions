class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                print(f'{prices[right]} - {prices[left]} = {prices[right] - prices[left]}')
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                print(max_profit)
                right+=1
            else:
                left = right
                right+=1
        
        return max_profit