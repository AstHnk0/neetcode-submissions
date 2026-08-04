# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n
        while L <= R:
            mid = (L + R) // 2
            if guess(mid) == -1:
                R = mid - 1
            elif guess(mid) == 1:
                L = mid + 1
            else:
                return mid
        return -1

        