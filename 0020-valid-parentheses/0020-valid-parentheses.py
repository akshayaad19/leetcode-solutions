class Solution:
    def isValid(self, s: str) -> bool:
        validlist = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in "{[(":
                validlist.append(c)
            else:
                if len(validlist) == 0:
                    return False
                if pairs.get(c) != validlist.pop():
                    return False
        return len(validlist) == 0