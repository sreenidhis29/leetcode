# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x: int):
        less = ListNode(0)
        greater = ListNode(0)
        p1, p2 = less, greater
        cur = head
        while cur:
            if cur.val < x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            cur = cur.next
        p2.next = None
        p1.next = greater.next
        return less.next
        
