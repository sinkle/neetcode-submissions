class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        for i in s:
            if i == ')':
                if not r or r.pop() != '(':
                    return False
            elif i == '}':
                if not r or r.pop() != '{':
                    return False
            elif i == ']':
                if not r or r.pop() != '[':
                    return False  
            else:     
                r.append(i)

        if r:
            return False

        return True     