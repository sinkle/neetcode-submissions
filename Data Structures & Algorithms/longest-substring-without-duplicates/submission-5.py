class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s = 0
        i, j = 0, 0
        keys = {}
        while j < len(s):
            if s[j] not in keys:
                keys[s[j]] = j
                j += 1
                max_s = max(max_s, j - i)
            else:
                rep_i = keys[s[j]]
                for w in range(i, rep_i + 1):
                    keys.pop(s[w])
                i = rep_i + 1
                keys[s[j]] = j
                j += 1
        return max_s


