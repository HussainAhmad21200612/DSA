
class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, n1, n2): 
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
     
        if n1.data != n2.data :
            return False
        return ((self.isIsomorphic(n1.left, n2.left)and
                self.isIsomorphic(n1.right, n2.right)) or
                (self.isIsomorphic(n1.left, n2.right) and
                self.isIsomorphic(n1.right, n2.left))
                )
