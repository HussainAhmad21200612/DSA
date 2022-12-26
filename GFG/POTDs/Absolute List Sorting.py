class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
    
class Solution:
    
    def sortList(self,head):
        start=head
        beg=head
      '''  # while(start!=None):
        #     if start.data>=0:
        #         newN=Node(start.data)
        #         if beg==None:
        #             beg=newN
        #             last=beg
        #         else:
        #             last.next=newN
        #             last=newN
        #     else:
        #         newN=Node(start.data)
        #         if beg==None:
        #             beg=newN
        #             last=beg
        #         else:
        #             newN.next=beg
        #             beg=newN
        #     start=start.next
        # return beg
        '''
        nextp=start.next
        if start==None:
            return head
        while nextp!=None:
            if nextp.data<0:
                beg=nextp.next
                start.next=beg
                nextp.next=head
                head=nextp
                nextp=beg
            else:
                nextp=nextp.next
                start=start.next
        return head
