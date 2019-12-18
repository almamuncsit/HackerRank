import itertools

S, k = input().split() 
S = sorted(S)
comb_list = []

for x in range(1, int(k)+1):
	combinations = list(itertools.combinations(S, x))
	comb_list += [ ''.join(combination) for combination in combinations ]

for comb in comb_list:
	print(comb)