class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        res = ListNode(None)
        node , s = res , [l1 , l2]
        while s[-1] :
            s.sort(key = lambda x:x.val)
            node.next= s[0]
            node = node.next
            s.append(s[0].next)
            s.pop(0)
        node.next = s[0]
        return res.next
