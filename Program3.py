#Subarray with given sum (POSITIVE NUMBER ONLY)
test_case = int(input("Enter test cases\n"))
for i in range(test_case):
	temp_user_input = input()
	temp_input = temp_user_input.split(' ')
	given_sum = int(temp_input[1])
	arr_length = int(temp_input[0])

	arr_input = input()
	arr = []
	arr_input = arr_input.split(" ")
	for i in arr_input:
		arr.append(int(i))
	
	header = 0
	temp_sum = 0
	flag = 0
	index = 0


	for i in arr:
		temp_sum = temp_sum + i
		index += 1
		while(temp_sum > given_sum):
			temp_sum = temp_sum - arr[header]
			header += 1
		if temp_sum == given_sum:	
			flag = 1	
			print("given sum is between {0} position and {1} position".format(header+1 ,index))
			break
	if flag == 0:
		print("-1")		
		
		