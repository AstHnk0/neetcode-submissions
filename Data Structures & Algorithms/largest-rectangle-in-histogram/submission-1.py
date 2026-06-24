class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        width = 1
        for i in range(len(heights)):
            min_h = heights[i]
            for j in range(i, len(heights)):
                    min_h = min(min_h, heights[j])
                    area = min_h * (j - i + 1)
                    max_area = max(area, max_area)
        return max_area



