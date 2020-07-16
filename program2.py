#Sum of  Subset
number = input("Enter number of set\n")

number = number.split()

numberList = []

for x in number:
	numberList.append(int(x))

lengthOfSet = len(numberList)

occurance =pow(2,lengthOfSet-1)


sum = 0
for y in numberList:
	sum = sum + int(y)*occurance
print(sum)	





