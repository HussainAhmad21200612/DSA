#include<algorithm>
class Solution{
    public:
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    int findPlatform(int arr[], int dep[], int n)
    {
    	// Your code here
    	sort(dep,dep+n);
    	sort(arr,arr+n);
    	int i=0,j=0,c=0,r=0;
    	while(i<n){
    	    if (arr[i]<=dep[j]){
    	        c++;
    	        i++;
    	        r=max(r,c);
    	    }
    	    else if(arr[i]>dep[j]){
    	        c--;
    	        j++;
    	    }
    	    
    	}
    	return r;
    }
};
