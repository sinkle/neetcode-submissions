class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        not_lett = (' ', '?', '.', ',', '!', ':', ';', "'")
        while i < j:
            if s[i] in not_lett:
                i += 1
                continue
            if s[j] in not_lett:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True