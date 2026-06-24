class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self, head = None, size = 0,):
        self.head = head
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head

        if index < self.size and self.head:
            for i in range(index):
                curr = curr.next
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if self.head:
            curr_node = self.head
            self.head = ListNode(val)
            self.head.next = curr_node
        else:
            self.head = ListNode(val)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            tail = curr

            tail.next = ListNode(val)
            tail = tail.next
        else:
            self.head = ListNode(val)

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index == self.size:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            self.size += 1

        elif index < self.size:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            tail_minus_1 = curr
            next_node = tail_minus_1.next
            tail_minus_1.next = ListNode(val)
            tail_minus_1.next.next = next_node
            self.size += 1

        elif index > self.size:
            pass


            

    def deleteAtIndex(self, index: int) -> None:
        if index != 0 and index < self.size:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1
        elif index == 0:
            self.head = self.head.next
        else:
            pass




        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)