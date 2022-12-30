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
        count+=1
        return True
