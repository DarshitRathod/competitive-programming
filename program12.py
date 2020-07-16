#Make given array in |a0 - a1| < |a1 - a2| < |a3 - a4|


testCases= int(input())
for _ in range(testCases):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	while a:	
		mid = len(a)//2
		print(a.pop(mid),end=" ")