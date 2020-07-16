from collections import defaultdict

class Graph:

	
	
	def __init__(self,node):
		self.graph = defaultdict(list)
		self.node = node
		
	def addEdges(self,src,dest):
		self.graph[src].append(dest)
		self.graph[dest].append(src)
	
	
	def dfsUtill(self,v,visited,parent):
	
		visited[v] = True

		for i in self.graph[v]:
			
			if visited[i] == False:
				if(self.dfsUtill(i,visited,v)):
					return True
			elif parent != i:
				return True
			
		return False
	
	
	def dfs(self,start):
		
		visited = [False]*self.node
		
		for i in range(self.node):
			if visited[i] == False:
				if(self.dfsUtill(i,visited,-1)) == True:
					return True



				
g = Graph(3)				

g.addEdges(0,1)
g.addEdges(1,2)

if(g.dfs(0)):
	print("Cycle")
else:
	print("Not Cycle")
