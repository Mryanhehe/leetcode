# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = head
        b = head
        for i in range(n):
            if a.next:
                a = a.next
            else:
                return head.next
        while a.next:
            a = a.next
            b = b.next
        b.next = b.next.next
        return head
        pass
