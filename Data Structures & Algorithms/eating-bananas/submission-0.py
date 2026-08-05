
class Solution:
    def canEat(self, piles, k) -> int:
        tmp = 0
        for n in piles:
            tmp += (n + k - 1) // k
        return tmp



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        answer = 0
        while L <= R:
            mid = (L + R) // 2
            if self.canEat(piles, mid) <= h:
                R = mid - 1
                answer = mid
            elif self.canEat(piles, mid) >= h:
                L = mid + 1
        return answer

                

        