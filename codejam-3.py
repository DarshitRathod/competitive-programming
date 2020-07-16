def fun(raw_arr):
	arr = []
	for i in range(len(raw_arr)):
		arr.append((raw_arr[i][0], raw_arr[i][1], i))
	arr.sort()
	cEnd = 0
	jEnd = 0
	res_arr = []
	for start, end, idx in arr:
		if start < cEnd and start < jEnd:
			return "IMPOSSIBLE"
		if start >= cEnd:
			res_arr.append(('C', idx))
			cEnd = end
		else:
			res_arr.append(('J', idx))
			jEnd = end
	res = ''
	for c, idx in sorted(res_arr, key=lambda x: x[1]):
		res += c
	return res
	
T = int(input())

for t in range(1, T + 1):
	N = int(input())
	arr = []
	for _ in range(N):
		interval = [int(s) for s in input().split(" ")]
		arr.append(interval)
	res = fun(arr)
	print("Case #{}: {}".format(t, res))