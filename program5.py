#Given max continuous  sum from array

inp = int(input("Enter Number of test cases: \n"))

for i in range(inp):
	arrSize = int(input("Enter Size of Array\n"))

	arrValueString = input("Enter Array value\n")

	arrSplited = arrValueString.split()
	if len(arrSplited) == arrSize:
		
		IntArr = []
		for i in arrSplited:
			IntArr.append(int(i))
			
		localSum = IntArr[0]
		globalSum = IntArr[0]		
		start = 0
		end = 0
		for i in range(1,arrSize):
			if (IntArr[i] > localSum+IntArr[i]):
				localSum = IntArr[i]
				start = i
				end = i
			else:
				localSum = localSum+IntArr[i]
				end = i-1
			if globalSum < localSum:
				globalSum = localSum
		print("Sum is ", globalSum)		
		print("Sum find between {0} and  {1}".format(start,end))		
				
		"""for i in range(1,arrSize):		
			localSum = max(IntArr[i],localSum+IntArr[i])
			globalSum = max(localSum,globalSum)			
		print("Sum is ", globalSum)"""
			



	
