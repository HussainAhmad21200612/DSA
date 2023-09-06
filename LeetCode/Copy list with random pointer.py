class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        # Base case, return early
        if not head:
            return head
        original_to_copy = {None: None}
        node = head
        while node:
            copy = Node(node.val)
            original_to_copy[node] = copy
            node = node.next
        node = head
        while node:
            copy = original_to_copy[node]
            nxt = original_to_copy[node.next]
            random = original_to_copy[node.random]
            copy.next, copy.random = nxt, random
            node = node.next
        return original_to_copy[head]
