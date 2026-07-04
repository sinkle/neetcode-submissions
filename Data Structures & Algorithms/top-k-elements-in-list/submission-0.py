class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        helper = {}
        for n in nums:
            if n not in helper:
                helper[n] = 0
            helper[n] += 1

        l = [(n, c) for n, c in helper.items()]
        sorted_l = sorted(l, key=lambda v: v[1], reverse=True)
        return [v[0] for v in sorted_l[:k]]