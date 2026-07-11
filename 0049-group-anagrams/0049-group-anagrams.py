class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            d.setdefault(key, []).append(strs[i])
        return list(d.values())  

        