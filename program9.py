for test in range(int(input())):
	counter = 0
	size = int(input())
	array = list(map(int,input().split()))
	if len(array) == size:
		sortArray = list(array)
		sortArray.sort()
		maxi = max(sortArray)
		occ = sortArray.count(maxi)
		for i in range(occ):
			sortArray.remove(maxi)
		
		k = sortArray[len(sortArray)-1]
		for i in range(1,len(array)-1):
			sum = k - array[i]
			if sum > 0:
				counter = counter + sum
	print(counter)