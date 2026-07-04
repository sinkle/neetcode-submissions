class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            s_sorted = ''.join(sorted(s)) 
            if s_sorted not in res:
                res[s_sorted] = []
            res[s_sorted].append(s)
        return list(res.values())