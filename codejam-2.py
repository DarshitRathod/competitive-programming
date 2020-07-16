


if __name__ == "__main__":
	
	test_case = int(input())
	ans = []
	for k in range(test_case):
		
		buff_str = []
		inp_str = input()
		
		inp_len = len(inp_str)
	
		i = 1
		
		temp  = []
		pre = inp_str[0]
		temp = ['(']*int(pre)
		buff_str.extend(temp)
		buff_str.append(pre)
		temp.clear()
		
		while(i<inp_len): 
			
			if(inp_str[i] == pre):
				buff_str.append(inp_str[i])
			else:				
				if(int(inp_str[i])>int(pre)):
					
					temp = [')']*int(pre)
					buff_str.extend(temp)
					temp.clear()
					
					temp = ['(']*int(inp_str[i])
					buff_str.extend(temp)
					
					buff_str.append(inp_str[i])
			
					temp.clear()
					
				else:
					temp = [')']*(int(pre)-int(inp_str[i]))
					buff_str.extend(temp)
					#print("String is buff_str",buff_str)
					buff_str.append(inp_str[i])
					#print("String is buff_str",buff_str)
					temp.clear()
			
			pre = inp_str[i]
			i+=1
			
			
		temp = [')']*int(pre)
		buff_str.extend(temp)
		temp.clear()
		ans.append("Case #{}: {}".format(k+1,"".join(map(str,buff_str))))
	
	
	for i in ans:
		print(i)	

	