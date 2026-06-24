class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 0
        for n in nums:
            if n == 1:
                current_streak += 1
            if n == 0:
                if max_streak < current_streak:
                    max_streak = current_streak
                current_streak = 0
            if max_streak < current_streak:
                max_streak = current_streak
        return max_streak

            
