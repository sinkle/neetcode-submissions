class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_i = 0
        r_i = len(s)-1
        skip_symbols = ['?', ' ', ',', '!', ':', ';', "'", '.']
        while l_i < r_i:
            if s[l_i] in skip_symbols:
                l_i += 1
                continue
            if s[r_i] in skip_symbols:
                r_i -= 1
                continue
            if s[l_i].lower() != s[r_i].lower():
                return False
            else:
                l_i += 1
                r_i -= 1
        
        return True

            