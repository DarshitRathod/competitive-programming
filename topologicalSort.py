from collections import defaultdict


class topologicalSort:



	def __init__(self,vertex):
		
		self.graph = defaultdict(list)
		self.st = []
		self.size = vertex
		
	def addEdge(self,src,dest):
		self.graph[src].append(dest)
		
	

	def topoLogicalUtill(self,v,visited):
	
		visited[v] = True		
		for i in self.graph[v]:		
			if visited[i] == False:
				self.topoLogicalUtill(i,visited)
		
		
		self.st.insert(0,v)
	

	def topoLogical(self):
	
		visited = [False]*self.size
		
		
		for i in range(node):		
			if visited[i] == False:
				self.topoLogicalUtill(i,visited)
		
				
if __name__ == "__main__":		
	
	testCase = int(input())
	
	while testCase:
		
		edge,node = map(int,input().split())
		g = topologicalSort(node)			
		graphList = list(map(int,input().split()))
		
		i = 0
		while i < len(graphList):
			g.addEdge(graphList[i],graphList[i+1])		
			i+=2	
		
		g.topoLogical()
		
		print(g.st)
		
		testCase-=1