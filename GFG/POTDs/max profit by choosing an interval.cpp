class Solution {
  public:
  static bool fun(vector<int>& a,vector<int>& b){
      if (a[1]<b[1]){
         return true;
      }else if (a[1]>b[1]){
         return false;
      }else{
          return a[0]<=b[0];
      }
  }
  int bS(vector<vector<int>> &arr,int k,int le){
      int l=0,end=le,mid,ind=-1;
      while(l<=end){
          mid=(l+end)/2;
          if(arr[mid][1]<=k){
              ind=mid;
              l=mid+1;
          }
          else{
              end=mid-1;
          }
      }
      return ind;
  }
    int maximum_profit(int n, vector<vector<int>> &arr) {
        // Write your code here.
        sort(arr.begin(),arr.end(),fun);
        vector<int> ans(n,0);
        ans[0]=arr[0][2];
        for(int i=0;i<n;i++){
            int ind=bS(arr,arr[i][0],i-1);
            if(ind==-1){
                ans[i]=arr[i][2];
            }
            else{
                ans[i]=ans[ind]+arr[i][2];
            }
            ans[i]=max(ans[i],ans[i-1]);
        }
        return ans[n-1];
    }
