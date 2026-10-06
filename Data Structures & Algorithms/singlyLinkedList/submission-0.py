class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        curr_idx = 0
        while curr:
            if curr_idx == index:
                return curr.val
            curr = curr.next
            curr_idx += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        curr_idx = 0
        while curr and curr_idx < index - 1:
            curr = curr.next
            curr_idx += 1
        if not curr or not curr.next:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
