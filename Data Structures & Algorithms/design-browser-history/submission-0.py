class ListNode:
    def __init__(self, url = "", next = None, prev = None):
        self.next = next
        self.prev = prev
        self.url = url


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for step in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                return self.curr.url
        return self.curr.url

    def forward(self, steps: int) -> str:
        for step in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                return self.curr.url
        return self.curr.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)