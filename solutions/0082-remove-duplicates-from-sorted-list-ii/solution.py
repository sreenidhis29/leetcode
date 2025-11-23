# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# LeetCode: Remove Duplicates from Sorted List II
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur:
            duplicate = False
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                duplicate = True
            if duplicate:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next
