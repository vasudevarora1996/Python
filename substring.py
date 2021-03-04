'''Given a string s, find the length of the longest substring without repeating characters.'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return ans
