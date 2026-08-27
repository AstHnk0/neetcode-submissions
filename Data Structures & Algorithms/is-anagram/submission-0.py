class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        for char in s:
            if char not in hashMapS:
                hashMapS[char] = 1
            else:
                hashMapS[char] += 1
        for char in t:
            if char not in hashMapT:
                hashMapT[char] = 1
            else:
                hashMapT[char] += 1
        if len(hashMapS) != len(hashMapT):
            return False
        if hashMapS != hashMapT:
            return False
        return True
        