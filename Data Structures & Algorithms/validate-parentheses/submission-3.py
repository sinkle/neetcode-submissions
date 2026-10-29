class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for sym in s:
            if sym in ('(', '{', '['):
                st.append(sym)
            else:
                if not st:
                    return False

                l_s = st.pop()
                if sym == ')':
                    if l_s == '(':
                        continue
                    return False

                if sym == ']':
                    if l_s == '[':
                        continue
                    return False
                if sym == '}':
                    if l_s == '{':
                        continue
                return False
        if st:
            return False
        
        return True

