
def knapsack(W,wt,V,n):

	dp = [[0 for i in range(W+1)] for j in range(n+1)]
	print(len(dp))
	
	for i in range(n+1):
		for j in range(W+1):
			if i==0 or j==0:
				dp[i][j] = 0
			elif(wt[i-1]<=j):
				dp[i][j] = max( V[i-1] + dp[i-1][j-wt[i-1]] , dp[i-1][j])
			else:
				dp[i][j] = dp[i-1][j] 
	print(dp)
	return dp[n][W]

if __name__ == "__main__":
	
	W = 5
	wt = [1,2,3]
	V = [6,10,12]
	ans = knapsack(W,wt,V,len(V))
	print(ans)
	
