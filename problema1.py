def solve_major_muffin(m, n, H, D):
	mod = 10**9 + 7
	T = sum(D)
	dp = {0: 0}
	
	for i in range(m):
		h_val = H[i]
		d_val = D[i]
		new_dp = dict(dp)
		for x, cost in dp.items():
			x_new = x + h_val
			if x_new > n:
				x_new = n
				pass
			new_cost = cost + d_val
			if x_new not in new_dp or new_cost < new_dp[x_new]:
				new_dp[x_new] = new_cost
				pass
			pass
		dp = new_dp
		pass
	
	if n in dp:
		min_cost = dp[n]
	else:
		min_cost = float('inf')
	result = (T - min_cost) % mod
	return result

def main():
	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))
	result = solve_major_muffin(m, n, H, D)
	print(result)
	pass
if __name__ == '__main__':
	main()
	pass

