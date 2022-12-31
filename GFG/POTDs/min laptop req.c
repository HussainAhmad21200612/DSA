#include<algorithm>
class Solution {
  public:
    int minLaptops(int N, int start[], int end[]) {
        // Code here
        sort(start,start+N);
        sort(end,end+N);
        int c=0,j=0,i=0,r=0;
        while(i<N){
            if (start[i]<end[j]){
                c++;
                i++;}
            else if (start[i]>=end[j]){
                c--;
                j++;}
            r=max(r,c);
        }
        return r;
        
    }
};
