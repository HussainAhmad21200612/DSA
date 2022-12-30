def sv(self,root,count):
        if root==None:
            return True
        left=singlevalued(root.left,count)
        right=singlevalued(root.right,count)
        
        if left==False or right==False:
            return False
        if root.left!=None and root.data!=root.left.data:
            return False
        if root.right!=None and root.data!=root.right.data:
            return False
        count[0]+=1
        return True
def singlevalued(self,root):
      count=[0]
      self.sv(root,count)
      return count[0]
