from collections import defaultdict



class DFS:

	def __init__(self,V):
		self.graph = defaultdict(list)
		self.V = V
	
	def addEdge(self,src,dest):
		self.graph[src].append(dest)


	def DFSUtill(self,i,visited):
		
		visited[i] = True
		
		print(i)
		
		for i in self.graph[i]:			
			if visited[i] == False:
				self.DFSUtill(i,visited)


	def dfs(self,graph):

		visited = [False]*len(self.graph)
		
		for i in range(len(self.graph)):
			
			if visited[i] == False:
				
				self.DFSUtill(i,visited)
	

		
if __name__ == "__main__":
	
	g = DFS(4)
	
	for i in range(4):
		src, dest = map(int,input().split())
		g.addEdge(src,dest)
		g.addEdge(dest,src)
		
	g.dfs(g.graph)	