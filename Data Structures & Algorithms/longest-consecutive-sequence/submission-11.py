class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        m = 0
        for n in nums:
            if n not in d:
                d[n] = d.get(n-1, 0) + d.get(n+1, 0) + 1
                d[n - d.get(n-1,0)] = d[n]
                d[n + d.get(n+1,0)] = d[n]
                m = max(m, d[n])
        return m