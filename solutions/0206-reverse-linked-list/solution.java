class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode curr = head;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = dummy.next;
            dummy.next = curr;
            curr = nextNode;
        }
        return dummy.next;
    }
}
