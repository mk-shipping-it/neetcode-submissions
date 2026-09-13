class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # if the selling day price is less than the currently thought buying price
        # new buying price = the lower selling price
        # BUYING CHEAPER IS ALWAYS BETTER

        max_days = len(prices)
        left, right, profit = 0, 1, 0

        while right < max_days:
            if prices[right] <= prices[left]:
                left = right
                right+=1
            else:
                profit = max(profit, prices[right] - prices[left])
                right+=1

        return profit