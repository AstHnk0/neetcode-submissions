class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        L, R = 0, len(newS) - 1
        while L < R:
            if newS[L] != newS[R]:
                return False
            L += 1
            R -= 1
        return True
            

