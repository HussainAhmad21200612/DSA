class Solution:
    def compute(self,head):
        def rev(s):
            pre=None
            curr=s
            # nex=cur
            while(curr):
                nex=curr.next
                curr.next=pre
                pre=curr
                curr=nex
            return pre
        # print(head.next)
        temp=rev(head)
        start=Node(temp.data)
        pre=start
        temp=temp.next
        while(temp):
            if temp.data>=pre.data:
                ne=Node(temp.data)
                pre.next=ne
                pre=ne
            temp=temp.next
        return rev(start)
