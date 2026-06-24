class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_right = 0
            for right_i in range(i + 1, len(arr)):
                if arr[right_i] > max_right:
                    max_right = arr[right_i]
            arr[i] = max_right
        arr[-1] = -1
        return arr