from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            heap.append((distance, [x, y]))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            result.append(point)
        return result

