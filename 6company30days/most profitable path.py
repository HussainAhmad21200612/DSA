class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(lambda:[])
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        def bp(b):
            stack.append(b)
            # print(stack)
            if b == 0:
                # print(stack)
                return stack
            visited.add(b)
            for i in graph[b]:
                if i not in visited:
                    t = bp(i)
                    if t:
                        return t
            visited.remove(b)
            stack.pop()
            
         
        stack = []
        S=bp(bob)
        # print(S)
        blen = len(S)-1
        gate = [0]*(len(edges)+1)
        visited=set()
        self.income = float('-inf')
        def dfs(alice, b, net):
            if len(graph[alice]) == 1 and graph[alice][0] in visited:
                self.income = max(self.income,net)
            
            visited.add(alice)   
            for n in graph[alice]:
                if n in visited:continue
                gate[S[min(b+1,blen)]] = 1
                if n == S[min(b+1,blen)]:
                    
                    dfs(n,min(b+1,blen),net + (amount[n]/2))
                else:
                    if gate[n]:
                        # print(net,n)
                        dfs(n,min(b+1,blen),net)
                    else:
                        # print(net,n)
                        dfs(n,min(b+1,blen),net + amount[n])
                gate[S[min(b+1,blen)]] = 0
            
            
        gate[bob] = 1   
        dfs(0,0,amount[0])
        
        return int(self.income)
