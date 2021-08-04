class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        current_min = prices[0]
        for price in prices:
            if current_min > price:
                current_min = price
            elif price - current_min > max_prof:
                max_prof = price - current_min
        return max_prof