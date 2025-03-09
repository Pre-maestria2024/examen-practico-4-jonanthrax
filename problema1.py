def solve_major_muffin(m, n, H, D):
	dp = [-float('inf')] * (n + 1)
	dp[0] = 0
	
	for i in range(m):
		h_i, d_i = H[i], D[i]
		for k in range(n, -1, -1):
			if dp[k] == -float('inf'):
				continue
			new_health = min(k + h_i, n)
			dp[new_health] = max(dp[new_health], dp[k])
			if k == n:
				dp[n] = max(dp[n], dp[k] + d_i)
				pass
			pass
		pass
	
	return dp[n] if dp[n] != -float('inf') else 0

def main():
	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))
	result = solve_major_muffin(m, n, H, D)
	print(result)
	pass
if __name__ == '__main__':
	main()
	#print(1)
	pass
