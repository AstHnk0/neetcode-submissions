class Heap:
    def __init__(self):
        self.heap = [0]

    def percolateDown(self, i):
            while 2 * i < len(self.heap):
                if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] > self.heap[2 * i] and self.heap[i] < self.heap[2 * i + 1]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] < self.heap[2 * i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
    def percolateUp(self, i):
        while i > 1:
            parent = i // 2
            if self.heap[i] > self.heap[parent]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = tmp
                i = parent
            else:
                break


    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
            self.percolateDown(i)
            cur -= 1
    def pop(self):
        maxValue = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.percolateDown(1)
        return maxValue
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        self.percolateUp(i)
        return val





class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = Heap()
        h.heapify(stones)
        while len(h.heap) > 2:
            firstStone = h.pop()
            secondStone = h.pop()
            result = abs(firstStone - secondStone)
            if result > 0:
                h.insert(result)

        return h.pop() if len(h.heap) > 1 else 0

