class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curcolor = image[sr][sc]
        visit = set()
        def dfs(image, sr, sc, color):
            if curcolor == color:
                return image
            ROWS, COLS = len(image), len(image[0])
            if min(sr,sc) < 0 or sr == ROWS or sc == COLS or (sr,sc) in visit or image[sr][sc] != curcolor:
                return
            if image[sr][sc] == curcolor:
                image[sr][sc] = color
            visit.add((sr,sc))
            dfs(image, sr + 1, sc, color)
            dfs(image, sr - 1, sc, color)
            dfs(image, sr, sc + 1, color)
            dfs(image, sr, sc - 1, color)

            return
        dfs(image, sr, sc, color)
        return image

