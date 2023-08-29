class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if head == None:
            return None
        curr = head
        while curr != None:
            newNode = Node(curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        curr = head
        while curr != None:
            if curr.arb != None:
                curr.next.arb = curr.arb.next
            curr = curr.next.next
        curr = head
        clonedHead = head.next
        clonedCurr = clonedHead
        while clonedCurr.next != None:
            curr.next = curr.next.next
            clonedCurr.next = clonedCurr.next.next
            curr = curr.next
            clonedCurr = clonedCurr.next
        curr.next = None
        clonedCurr.next = None
        return clonedHead
