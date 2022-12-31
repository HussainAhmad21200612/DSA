class Solution:
    def dfs(self,grid,x,y,r,c,z):
        if x<0 or x>=r or y<0 or y>=c or grid[x][y]==-1:
            return 0
        if grid[x][y]==2:
            if z==-1:
                return 1 
            else:
                return 0
        grid[x][y]=-1
        z-=1
        tot_p=self.dfs(grid,x+1,y,r,c,z)+self.dfs(grid,x-1,y,r,c,z)+self.dfs(grid,x,y+1,r,c,z)+self.dfs(grid,x,y-1,r,c,z)

        grid[x][y]=0
        z+=1

        return tot_p
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        noOfZeros=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0: noOfZeros+=1
                elif grid[i][j]==1:
                    target_x,target_y=i,j
        return self.dfs(grid,target_x,target_y,row,col,noOfZeros)
                
