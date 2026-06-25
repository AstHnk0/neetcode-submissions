class ListNode:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.size = 0

    def get(self):
        return self.head.val

    def enqueue(self, val):
        newNode = ListNode(val)

        if self.head:
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            self.head = self.tail = newNode
        self.size += 1

    def dequeue(self):
        if not self.head:
            return None
        if self.head:
            self.head = self.head.next
            self.size -= 1
        if not self.head:
            self.tail = None
    
    def dequeue_to_end(self):
        if not self.head or not self.head.next:
            return None
        curr = self.head
        self.head = self.head.next
        self.tail.next = curr
        self.tail = self.tail.next
        self.tail.next = None

    
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = Queue()
        for student in range(len(students)):
            queue.enqueue(students[student])
        rejections = 0
        i = 0
        while queue.size > 0 and rejections < queue.size and i < len(sandwiches):
            if sandwiches[i] == queue.get():
                i += 1
                queue.dequeue()
                rejections = 0

            else:
                rejections += 1
                queue.dequeue_to_end()

        return queue.size