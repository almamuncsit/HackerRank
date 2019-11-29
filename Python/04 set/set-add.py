
def distinct_stamps(n):
	stamp = set()
	while n > 0:
		stamp.add( input() )
		n-=1
	return stamp


if __name__ == '__main__':
	n = int( input() )
	print( len(distinct_stamps(n)) )