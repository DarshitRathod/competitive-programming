import sys
def coinChange(D,V):

	table = [0 for i in range(V+1)] #make array of size V+1 (0..V) and fill 0
	
	table[0] = 0 #it indicates that we require 0 coins to form 0 rupees
	
	for i in range(1,V+1):  #set infinite or max value to table starting from 1 to V+1
		table[i] = sys.maxsize

	res = 0
	for i in range(1,V+1): #Rupees Loop
		
		for j in range(len(D)): #Denomination Loop
		
			if D[j] <= i: #if denomination is small than rupees than only we are allowed to make that rupees
			
				res =  table[i-D[j]] # subtract rupees from denomination so we get remaining rupees and remaining rupees value is retrieve from previous value
				if res != sys.maxsize and res + 1 < table[i]: # check res is not max and res + 1 should less than table[i]
					table[i] = res + 1 # add number of coins in table[i] and + 1 becaus we using current denomination and remaining from previous 


	return table[V] # last index is answer


if __name__ == "__main__":

	D = [7,2,3,6]
	V = 13
	ans = coinChange(D,V)
	print(ans)