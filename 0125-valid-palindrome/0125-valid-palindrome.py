class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = ""
        t = ""
        for i in s:
            if i.isalnum() == True:
                f+=i
                t+=i

        f = f[::-1]
        print(f)
        print(t)
        if(t == f):
            return True
        return False
