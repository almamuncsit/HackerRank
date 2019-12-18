import itertools

print( [k for k, g in itertools.groupby('AAAABBBCCDAABBB')])
print([list(g) for k, g in itertools.groupby('AAAABBBCCD')])

for k, g in itertools.groupby('AAAABBBCCD'):
	print(k)
	print(len(list(g)))