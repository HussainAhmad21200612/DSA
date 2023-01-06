bool a=false;
vector<int> prime(10000,1);
class Solution{   
  public:
  void seive(){
      for(int i=2;i<10000;i++){
          for(int j=i+i;j<10000;j=j+i){
              prime[j]=0;
          }
      }
      
  }
    int shortestPath(int Num1,int Num2)
    {   
        // Complete this function using prime vector
        if(!a){
            seive();
            a=true;
        }
        queue<pair<int,int>> qu;
        qu.push({Num1,0});
        vector<int> visited(10000,0);
        visited[Num1]=1;
        while(qu.size()){
            auto t=qu.front();
            qu.pop();
            if(t.first==Num2) return t.second;
            string n=to_string(t.first);
            for(int i=0;i<4;i++){
                for(int j=0;j<=9;j++){
                    char c='0'+j;
                    string n2=n;
                    n2[i]=c;
                    int temp=stoi(n2);
                    if(prime[temp] and n2[0]!='0' and visited[temp]==0){
                        qu.push({temp,t.second+1});
                        visited[temp]=1;
                    }
                }
            }
        }
        return -1;
    }
};
