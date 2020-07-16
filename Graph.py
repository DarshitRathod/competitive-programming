from collections import defaultdict
"""Creation of Graph """
"""
class nodeCreate:

	def __init__(self,data):
		self.val = data
		self.next = None




class addEdge:
	
	def __init__(self,totalVertex):
		self.V = totalVertex
		self.li = [None]*self.V

	def addEd(self,src,dest):
		
		#for src to destination
		node = nodeCreate(dest)
		node.next = self.li[src]
		self.li[src] = node
		
		#for destination to source
		node = nodeCreate(src)
		node.next = self.li[dest]
		self.li[dest] = node
		
	def printGraph(self):
		for i in range(self.V):
			x = self.li[i]
			print("list index {}\n Head".format(i),end="")
			while x:
				print("  -> {}".format(x.val),end="")
				x = x.next
			print("\n")	
g = addEdge(5)

g.addEd(0,1)
g.addEd(0,4)
g.addEd(1,2)
g.addEd(1,3)
g.addEd(1,4)
g.addEd(2,3)		
g.addEd(3,4)

g.printGraph()		"""
		
""" BFS Traversal of Graph """


class BFS:

	"""Creation of Graph"""
	def __init__(self):
		self.graphT = defaultdict(list)
	
	def addEdge(self,src,dest):
		self.graphT[src].append(dest)
	
	def bfs(self,start):	
		visited = [False] * (len(self.graphT))
		q = []
		
		q.append(start)
		visited[start] = True
		
		while q:
			
			s = q.pop(0)
			print("visited -> {} ".format(s))
			
			for i in self.graphT[s]:
				if visited[i] == False:
					q.append(i)
					visited[i] = True


class DFS:

	def __init__(self):
		self.graph = defaultdict(list)
		
	def addEd(self,src,dest):
		self.graph[src].append(dest)
		
	def DFSUtill(self,i,visited):
		visited[i] = True
		print(i)
		
		for i in self.graph[i]:
			if visited[i] == False:
				self.DFSUtill(i,visited)
	
	def dfs(self):
		visited = [False]*(len(self.graph))
		
		for i in range(len(self.graph)):
			if visited[i] == False:
				self.DFSUtill(i,visited)
		
			

					
"""gr = DFS()

gr.addEd(0, 1) 
gr.addEd(0, 2) 
gr.addEd(1, 3) 
gr.addEd(4, 1) 
gr.addEd(6, 4) 
gr.addEd(5, 6)
gr.addEd(5, 2)
gr.addEd(6, 0)
gr.dfs() """
	
	
	
#Find Mother Vertex 	





class motherVertex:

	def __init__(self,v):
		self.V = v
		self.graph = defaultdict(list)
		
	def addEd(self,src,dest):
		self.graph[src].append(dest)
		
	
	def DFSUtill(self,i,visited):
		
		visited[i] = True
		
		for i in self.graph[i]:
			if visited[i] == False:
				self.DFSUtill(i,visited)

	def findMother(self):
	
		visited = [False] * self.V
		
		
		for i in range(self.V):
			if visited[i] == False:
				self.DFSUtill(i,visited)
				track = i 
	
	
	
		visited = [False] * self.V
		
		self.DFSUtill(track,visited)
		
		if any(i == False for i in visited):
			print("Mother Vertex Not Found")
		else:	
			print("Mother Vertex is " + str(track))


gr = motherVertex(7)

gr.addEd(0, 1) 
gr.addEd(0, 2) 
gr.addEd(1, 3) 
gr.addEd(4, 1) 
gr.addEd(6, 4) 
gr.addEd(5, 6)
gr.addEd(5, 2)
gr.addEd(6, 0)

gr.findMother()	