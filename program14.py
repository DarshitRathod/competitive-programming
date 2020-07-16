



test_case = int(input())

while test_case:
	
	inp = int(input())
	if(inp%4 != 0):
		print("NO")
	else:
		print("YES")
		for i in range(2,inp+1,2):
			print(i,end=" ")
		for i in range(1,inp-1,2):
			print(i,end=" ")	
		print(inp+inp//2-1)
	test_case-=1