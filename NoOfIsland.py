class isLand:


	def __init__(self,row,col,graph):
		self.row = row
		self.col = col
		self.graph = graph


	def isSafe(self,i,j,visited):

		return(i>=0 and i<self.row and j>=0 and j<self.col and not visited[i][j] and self.graph[i][j])

	def dfs(self,i,j,visited):
	
		visited[i][j] = True
		
		rwNum = [-1,-1,-1,0,0,1,1,1]
		colNum = [-1,0,1,-1,1,-1,0,1]
		
		
		for k in range(8):
			if self.isSafe(i+rwNum[k],j+colNum[k],visited):
				self.dfs(i+rwNum[k],j+colNum[k],visited)
	
	
	
	
	def countIsland(self):
		
		visited = [[False for i in range(self.col)] for j in range(self.row)]
		
		count = 0
		for i in range(self.row):
			for j in range(self.col):			
				if visited[i][j] == False and self.graph[i][j] == 1:
					self.dfs(i,j,visited)
					
					count+=1



		return count






graph = [
			[1,1,0,0,0],
			[0,1,0,0,1],
			[1,0,0,1,1],
			[0,0,0,0,0],
			[1,0,1,0,1]
		]
		
g  = isLand(len(graph),len(graph[0]),graph)		

print(g.countIsland())