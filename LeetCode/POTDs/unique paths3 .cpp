class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int t_x,t_y,noOfz=0,row=grid.size(),col=grid[0].size();
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if (grid[i][j]==0){
                noOfz+=1;
                }
                else if (grid[i][j]==1){
                    t_x=i;
                    t_y=j;
                }
            }
        }
        int ans=0;
        int z=0;
        dfs(grid,t_x,t_y,row,col,z,noOfz,ans);
        return ans;
    }
    void dfs(vector<vector<int>>& grid,int x,int y,int r,int c,int z,int& noOfz,int& ans){
        if (x<0 || x>=r || y<0 || y>=c || grid[x][y]==-1){
            return ;
        }
        if(grid[x][y]==2){
            if (z-1==noOfz)
            ans+=1;
            return ;
        }
        grid[x][y]=-1;
        vector<pair<int,int>>dir={{0,1},{1,0},{-1,0},{0,-1}};
        for(pair<int,int>p:dir){
            int i=x+p.first;
            int j=y+p.second;
            if (x>=0 && x<r && y>=0 && y<c){
                dfs(grid,i,j,r,c,z+1,noOfz,ans);
            }
        }
       
        grid[x][y]=0;
        
        
    }
};
