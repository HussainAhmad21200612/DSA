class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        def binarys(r,l,h):
        #  if l<=h:
                
        #     mid=(l+h)//2
        #     if matrix[r][mid]==target:
        #         return 1
        #     elif matrix[r][mid]<target:
        #         binarys(r,mid+1,h)
        #     else:
        #         binarys(r,l,mid-1)
        #  else:
        #     print(matrix[r][l-1])
        #     return 0
            l1=matrix[r]
            for i in range(n):
                mid=(l+h)//2
                if l1[mid]==target:
                    return 1
                elif l1[mid]>target:
                    h=mid-1
                else:
                    l=mid+1
            return 0
        for i in range(m):
            if matrix[i][0]==target or matrix[i][n-1]==target:
                return True
            if matrix[i][0]<target and matrix[i][n-1]>target:
                return bool(binarys(i,1,n-2))
        
