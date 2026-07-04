class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_ = prices[0]
        left, right = 0, 1
        while right < len(prices):
            if prices[right] > prices[left]:
                res = max(res, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1

        return res