class Solution:

    def encode(self, strs: List[str]) -> str:
        len_strs = len(strs)
        h = [s if s else "!!!" for s in strs]
        return '+-+-+'.join(h)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = s.split('+-+-+')
        return ['' if s == "!!!" else s  for s in res]
