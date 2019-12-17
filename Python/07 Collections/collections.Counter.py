from collections import Counter

X = int(input())
shoes = Counter( input().split() )

N = int( input() )
total = 0
for _ in range(0, N):
	size, price = input().split()
	if shoes[size] > 0:
		total = total + int(price)
		shoes[size] = shoes[size] - 1

print(total)