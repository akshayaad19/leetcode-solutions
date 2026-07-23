class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countchar = {}
        left = 0
        best = 0
        for right, c in enumerate(s):
            countchar[c] = countchar.get(c, 0) + 1
            while (right - left + 1) - max(countchar.values()) > k:
                countchar[s[left]] -= 1
                left += 1
            if (right - left + 1) > best:
                best = right - left + 1
        return best