#Pythagorean Triplet



if __name__ == '__main__':

	inp = list(map(int,input().split()))
	flag = 0
	
	for i in range(len(inp)):
		inp[i] = inp[i]*inp[i]
	
	inp.sort()
	
	for i in range(len(inp)-1,1,-1):
	
		j = 0
		k = i - 1
		
		while(j<k):
		
			if(inp[j]+inp[k] == inp[i]):
				flag = 1
				break
			else:
				if(inp[j]+inp[k] < inp[i]):
					j = j+1
				else:
					k = k - 1
		
	
	print("True") if(flag == 1) else print("False")	
	