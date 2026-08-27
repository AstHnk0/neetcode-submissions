class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


        
        

    def get(self, key: int) -> int:
            if key in self.cache:
                node = self.cache[key]
                #cut from old place
                node.next.prev = node.prev
                node.prev.next = node.next

                #put to the new place
                node.next = self.right
                node.prev = self.right.prev

                self.right.prev.next = node
                self.right.prev = node
                return node.val
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.cache[key] = node
            node.prev = self.right.prev
            node.next = self.right

            self.right.prev.next = node
            self.right.prev = node

        else:
            node = self.cache[key]
            node.val = value
            #cut from old place
            node.prev.next = node.next
            node.next.prev = node.prev

            #put to new place
            node.next = self.right
            node.prev = self.right.prev

            self.right.prev.next = node
            self.right.prev = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next