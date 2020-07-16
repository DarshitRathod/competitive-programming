#merge 2 sorted array using library

"""
from heapq import merge
for _ in range(int(input())):
	p,q=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c=list(merge(a,b))
print(c)	"""


#merge 2 sorted array using core logic

print("Enter Size of 2 array (space separated)")

l1,l2 = map(int,input().split())

arr1 = []
arr2 = []

for i in range(l1):
	temp = int(input())
	arr1.append(temp)
	
for i in range(l2):
	temp = int(input())
	arr2.append(temp)	
		
for i in range(l2):
	for j in range(l1):
		if (arr2[i] > arr1[j]):
			temp = arr1[j]
			arr1[j] = arr2 [i]
			arr2[i] = temp
			
arr1.sort()			
print(arr2,arr1)			