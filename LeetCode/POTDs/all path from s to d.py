class Solution:
    # def dfs(self,graph,path,visited,ans,curr):
        
    #     path.append(curr)
    #     visited[curr]= True
    #     if curr==len(graph)-1:

    #         ans.append(path)
    #     for i in graph[curr]:
    #         if visited[i]==False:
    #             self.dfs(graph,path,visited,ans,i)
    #     visited[curr]=False
    #     path.pop()
    def allPathsSourceTarget(self, graph):
        def dfs(i, cur):
            if i == nodes - 1:
                result.append(cur[:])
                return

            for j in graph[i]:
                dfs(j, cur + [j])

        nodes = len(graph)
        result = []
        dfs(0, [0])
        return result
        # # ans=[[]]
        # # path=[]
        # visited=[False]*len(graph)
        # self.dfs(graph,path,visited,ans,0)
        # return ans
