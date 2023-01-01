class Solution{
    	public:
    	int mod=1000000007;
    long long int inverse(long long int i){
        if (i==1){
            return 1;
        }
        return (mod-((mod/i)*inverse(mod%i))%mod+mod)%mod;
    }

	int compute_value(int n)
	{
	    // Code here
	    long long int ncr=1,ans=1;
	    for(int i=1;i<=n;i++)
	    {
	        ncr=(((ncr*(n-i+1))%mod)*inverse(i))%mod;
	        ans=(ans+(ncr*ncr)%mod)%mod;
	    }
	    return ans;
	}
};
