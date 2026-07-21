class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0 
        window = set()
        lenmax = 0 
        for right, c in enumerate(s):
            if c not in window:
                window.add(c)
            else:  
                while c in window:
                        window.remove(s[left])
                        left += 1
                window.add(c)
            if len(window) > lenmax:
                lenmax = len(window)

        return lenmax