# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0, head)
        prev = dummy
        while True:
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            cur = prev.next
            nxt = cur.next
            for _ in range(k - 1):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next
            prev = cur
