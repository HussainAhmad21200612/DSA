class Solution {
public:
    int nthUglyNumber(int n) {
       int p2=0,p3=0,p5=0;
       vector<int>dp(n);
       dp[0]=1;
       for(int i=1;i<n;i++){
           int mul_2=dp[p2]*2;
           int mul_3=dp[p3]*3;
           int mul_5=dp[p5]*5;
           dp[i]=min(mul_2,min(mul_3,mul_5));
           if(dp[i]==mul_2){
               p2++;
           }
           if(dp[i]==mul_3){
               p3++;
           }
           if(dp[i]==mul_5){
               p5++;
           }
       }
       return dp[n-1];
    }
};
