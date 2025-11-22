class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mp = {}
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            node = mp[cur]
            node.next = mp.get(cur.next)
            node.random = mp.get(cur.random)
            cur = cur.next
        return mp[head]
