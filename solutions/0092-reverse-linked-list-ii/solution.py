class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        nxt = None
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
