class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
        # Code here
        n = len(grid)
        m = len(grid[0]) 
        q = [] 
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append([i, j])
                    grid[i][j] = 0 
                else:
                    grid[i][j] = float("inf") 
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1] 
        while len(q): 
            top = q.pop(0)
            x = top[0]
            y = top[1]
            time = grid[x][y]
            for i in range(4):
                newx = x + row[i]
                newy = y + col[i]
                if newx >= 0 and newx < n and newy >= 0 and newy < m and grid[newx][newy] == float("inf"): 
                    grid[newx][newy] = time + 1 
                    q.append([newx, newy])
        return grid 
