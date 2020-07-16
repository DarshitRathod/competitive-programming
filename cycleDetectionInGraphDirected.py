from collections import defaultdict

class Graph:
	
	
	def __init__(self,node):
		self.graph = defaultdict(list)
		self.node = node
		
	def addEdges(self,src,dest):
		self.graph[src].append(dest)
		
	
	
	def dfsUtill(self,v,visited):
	
		visited[v] = True

		for i in self.graph[v]:
			
			if visited[i] == False:
				if(self.dfsUtill(i,visited) == True):
					return True
			else:
				return True
			
		return False
	
	
	def dfs(self,start):
		
		visited = [False]*self.node
		
		for i in range(self.node):
			if visited[i] == False:
				if(self.dfsUtill(i,visited)) == True:
					return True



				
g = Graph(5)				

g.addEdges(0,1)
g.addEdges(0,2)
g.addEdges(2,3)
g.addEdges(2,4)
g.addEdges(3,1)

if(g.dfs(0)):
	print("Cycle")
else:
	print("Not Cycle")
