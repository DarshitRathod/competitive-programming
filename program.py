

listNumber = [4,-2,1,-5,5]
listIndex = []
negativeList = []

for i in range(len(listNumber)):
	if listNumber[i]<0:
		listIndex.append(i)
for j in range(len(listIndex)):
	negativeList.append(listNumber[listIndex[j]])

for k in range(len(negativeList)):
	listNumber.remove(negativeList[k])
listNumber.sort()
for j in range(len(negativeList)):
	listNumber.insert(listIndex[j],negativeList[j])

print(listNumber)	