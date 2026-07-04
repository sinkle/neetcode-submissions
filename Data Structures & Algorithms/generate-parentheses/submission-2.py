class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(r, o, c):
            if len(r) == 2 * n:
                res.append(r)
                return
            
            if o < n:
                backtrack(r + '(', o + 1, c)
            
            if c < o:
                backtrack (r + ')', o, c + 1)
            
        backtrack('', 0, 0)
        return res

