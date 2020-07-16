#Given a 2 string find how many minimum operation require to convert one string to another.





if __name__ == "__main__":


	str1 = "abcdef" #String which we want to convert in another string 
	str2 = "azced" #Destination String 
	
	table = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

	
	
	
	for i in range(len(str2)+1):
		for j in range(len(str1)+1):
			if i == 0:
				table[i][j] = j
			elif j == 0:	
				table[i][j] = i
			elif str2[i-1] == str1[j-1]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = min(table[i][j-1] , table[i-1][j-1] , table[i-1][j]) + 1
	
	print(table[len(str2)][len(str1)])


