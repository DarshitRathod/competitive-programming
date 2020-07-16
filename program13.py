t=int(input())


for i in range(t):
	k = 3
	inp = int(input())
	while(inp%k != 0):
		k = k * 2 + 1
		break
	print(inp//k)	