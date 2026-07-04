class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return self._with_index(s, t)
        return self._with_dict(s, t)
        # return self._by_sorted(s, t)
        
    @staticmethod
    def _with_index(s: str, t: str):
        if len(s) != len(t):
            return False
        i = 0
        counter = {}
        for i in range(len(s)):
            s_el = s[i]
            if s_el not in counter:
                counter[s_el] = 0
            counter[s_el] += 1

            t_el = t[i]
            if t_el not in counter:
                counter[t_el] = 0
            counter[t_el] -= 1
        
        for n in counter.values():
            if n != 0:
                return False
        
        return True 

    @staticmethod
    def _with_dict(s: str, t: str):
        counter = {}
        for s_el in s:
            if s_el not in counter:
                counter[s_el] = 0
            counter[s_el] += 1
        
        for t_el in t:
            if t_el not in counter:
                return False
            counter[t_el] -= 1
        
        for n in counter.values():
            if n != 0:
                return False
        
        return True 
        
    @staticmethod
    def _by_sorted(s: str, t: str):
        tt = sorted(t)
        ss = sorted(s)
        return ss == tt
        