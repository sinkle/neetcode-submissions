class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                c_b = 0
                i = n - 1
                while d.get(i):
                    c_b = max(d[i], c_b)
                    i -= 1
                 
                i = n + 1
                c_a = 0
                while d.get(i):
                    c_a = max(d[i], c_a)
                    i += 1 
                d[n] = c_b + c_a + 1

        return max(d.values()) if d else 0