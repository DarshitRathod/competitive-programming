

arr=  [5,5,10,100,10,5]



incl = arr[0]
excl = 0


for i in range(1,len(arr)):
	
	pre_incl = incl
	incl = excl + arr[i]
	excl = max(pre_incl,excl)
	
print(max(incl,excl))	