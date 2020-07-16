s = "092282"
k = 3
strr = [i for i in s]
ptr = strr
for i in range(int(len(strr)/2)):
	if(strr[i] != strr[len(strr)-1-i]):
		temp = max(strr[i],strr[len(s)-1])
		ptr[i] = ptr[len(s)-1-i] = temp
		k-=1
print(ptr)