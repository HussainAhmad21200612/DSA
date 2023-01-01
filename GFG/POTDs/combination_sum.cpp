class Solution {
  public:
    //Function to return a list of indexes denoting the required 
    //combinations whose sum is equal to given number.
    void solution(int i,vector<int> cur,int target,vector<int> &a,vector<vector<int>> &ans){
        if(target==0){
            
            ans.push_back(cur);
            return;
        }
        if(i>=a.size() || target<0){
            return;
        }
        cur.push_back(a[i]);
        solution(i,cur,target-a[i],a,ans);
        cur.pop_back();
        solution(i+1,cur,target,a,ans);
        
    }
    vector<vector<int> > combinationSum(vector<int> &A, int B) {
        // Your code here
        sort(A.begin(),A.end());
        A.erase(unique(A.begin(), A.end()), A.end());
        vector<vector<int>> ans;
        vector<int> cur;
        solution(0,cur,B,A,ans);
        if (ans.size()==0){
            return ans;
        }
        else{
            
             sort(ans.begin(),ans.end());
             
             return ans;
        }
    }
};
