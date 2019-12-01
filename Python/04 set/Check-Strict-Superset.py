
def strict_superset(A):
	n = int( input() )
	for x in range(0, n):
		sub_set = set(input().split())
		if len(sub_set.difference(A)):
			return False

	return True


if __name__ == '__main__':
	A = set(input().split())
	if strict_superset(A):
		print('True')
	else:
		print('False')

