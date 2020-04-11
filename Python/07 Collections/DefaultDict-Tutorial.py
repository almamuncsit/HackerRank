from collections import defaultdict

n, m = input().split()
d = defaultdict(list)

for i in range(0, int(n)):
	d[input()].append(i+1)

for i in range(0, int(m)):
	item = input()
	if len(d[item]) == 0:
		print(-1)
	else:
		print(*d[item])
