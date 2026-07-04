class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {')': '(', '}': '{', ']': '['}
        stack = []
        for p in s:
            if p in map_:
                if not stack or stack.pop() != map_[p]:
                    return False
            else:
                stack.append(p)
        
        return not stack