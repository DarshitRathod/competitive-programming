



if __name__ == "__main__":

	arr = [10, 22, 9, 33, 21, 50, 41, 60] 
	
	LIS = [1 for i in range(len(arr))]
	
	
	for i in range(1,len(arr)):
		for j in range(0,i):
			if arr[i]>arr[j] and LIS[i] < LIS[j] + 1:
				LIS[i] = LIS[j] + 1
			
	print(max(LIS))		