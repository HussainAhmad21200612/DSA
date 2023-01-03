class Solution {
public:    
    unordered_map<int,vector<int>> mp;
    int height=0,maxAns=INT_MIN;
    void setHeight(int node,int bob,int h,vector<int>&visited){
        if(node==bob){
            height=h;
            return;
        }
        visited[node]=true;
        for(auto it:mp[node])
          if(!visited[it])
            setHeight(it,bob,h+1,visited);
    }
    
    bool updateValues(int node,int bob,int&count,bool even,vector<int>& amount,vector<int>&visited){
        if(node==bob){
           if(count==0){ 
              if(even)
                amount[node]/=2;
            }
            else if(count>0){
                amount[node]=0;
            }
            count--;
            return true;
        }
        
        visited[node]=true;

        for(auto it:mp[node]){
            if(!visited[it])
            if(updateValues(it,bob,count,even,amount,visited)){
                if(count==0){
           
                if(even)
                      amount[node]/=2;
                }
                else if(count>0){
                    amount[node]=0;
                }
                count--;
               return true; 
            }    
        }
        
        return false;
    }

    void DFS(int node,int sum,vector<int>& amount,vector<int>&visited){

        int next=mp[node].size();
        if((next==1)&&node!=0){
            maxAns=max(maxAns,sum);
            return;
        }
        
        visited[node]=true;
        for(auto it:mp[node]){
            if(!visited[it])
                DFS(it,sum+amount[it],amount,visited);
        }
    }
    
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        for(auto it:edges){
            mp[it[0]].push_back(it[1]);
            mp[it[1]].push_back(it[0]);
        }
        
        vector<int> visited1(amount.size(),0),visited2(amount.size(),0),visited3(amount.size(),0);
        setHeight(0,bob,0,visited1);
        int h=(height+1)/2;
        
        if(height&1)
            updateValues(0,bob,h,false,amount,visited2);
        else updateValues(0,bob,h,true,amount,visited2);
        
        DFS(0,amount[0],amount,visited3);
        return maxAns;
        
    }
};
