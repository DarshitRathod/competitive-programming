

def duplicate(matrix):
	matti = 0
	for i in range(rows):	
		if len(set(matrix[i])) != len(matrix[i]):		
			matti +=1 
	return matti
	

	
if __name__ == "__main__":
	
	test_case = int(input())
	ansFinal = []
	for it in range(test_case):		
		rows = int(input())		
		row = 0
		column = 0
		summ = 0
		matrix = [list(map(int,input().split())) for i in range(rows)]
		
		row = duplicate(matrix)
		
		for i in range(rows):
			summ  = summ + matrix[i][i]
			for j in range(i+1,rows):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]	
		
		column = duplicate(matrix)
		
		ansFinal.append("Case #{}: {} {} {}".format(it+1,summ,row,column))

for i in ansFinal:
	print(i)
		
	
	
	