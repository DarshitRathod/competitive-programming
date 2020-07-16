"""Given a sorted array of positive integers. 
Your task is to rearrange  the array elements alternatively 
i.e first element should be max value, second should be min value, third should be second max, 
fourth should be second min and so on.."""

testCases = int(input())
for i in range(testCases):
	sizeOfArray = int(input())
	for j in range(1):
		k = input()
		k = k.split()
		if len(k) == sizeOfArray:
			front = 0
			back = len(k)-1
			if len(k) % 2 == 0: 
				while(front!=back and front<back):
					print(k[back])
					back-=1
					print(k[front])
					front+=1
			else:
				while(front!=back):
					print(k[back])
					back-=1
					print(k[front])
					front+=1
				print(k[front])	
				