class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] < prices[j]:
                m = max(m, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return m
            