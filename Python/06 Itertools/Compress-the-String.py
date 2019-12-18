import itertools

print(*[ ( len(list(g)), int(k) ) for k, g in itertools.groupby(input()) ])