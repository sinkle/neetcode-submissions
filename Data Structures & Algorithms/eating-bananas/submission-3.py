class Solution:
    def _calc_hours(self, piles: List[int], k: int):
        h = 0
        for i in range(len(piles)):
            h += math.ceil(piles[i] / k)
        return h




    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r-l) // 2    
            new_h = self._calc_hours(piles, m)
            if new_h <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
            

                