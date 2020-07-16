#Find triplets 
#0 1 2 3 have triplet like 0 + 1 = 1 , 0 + 2 = 2, 1 + 2 = 3


def triplet(arr,no_of_input):
    arr.sort()
    arr = list(arr)
    max = arr[len(arr)-1]
    count = 0
    for i in range(no_of_input-1):
        for j in range(i+1,no_of_input-1):
            temp_sum = arr[i] + arr[j]
            if temp_sum > max:
                break
            if temp_sum in arr:
                count += 1
    print(count if count>0 else -1)



if __name__ == '__main__':
	print("Enter No. of test Cases:\n")
	no_of_testcase = int(input())
	for i in range(no_of_testcase):
		print("Enter Input length :\n")
		no_of_input = int(input())
		arr = []
		for i in range(1):
			print("Enter Input\n")
			k = input()
			k = k.split()
			if len(k) == no_of_input:
				for i in range(len(k)):
					arr.append(int(k[i]))
		triplet(arr,no_of_input)