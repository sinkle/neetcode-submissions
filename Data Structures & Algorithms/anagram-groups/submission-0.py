class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        helper = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in helper:
                helper[sorted_s] = []
            
            helper[sorted_s].append(s)
        
        return list(helper.values())
