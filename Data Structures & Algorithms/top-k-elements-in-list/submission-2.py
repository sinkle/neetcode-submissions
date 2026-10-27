class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        a = [[] for _ in range(len(nums)+1)]

        for n, c in cnt.items():
            a[c].append(n)

        res = []
        for v in a[::-1]:
            for i in v:
                res.append(i)
                if len(res) == k:
                    return res
