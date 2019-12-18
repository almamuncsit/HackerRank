import itertools

S, k = input().split() 
combinations = list(itertools.combinations_with_replacement(sorted(S), int(k)))
comb_list = [ ''.join(combination) for combination in combinations ]

for comb in comb_list:
	print(comb)