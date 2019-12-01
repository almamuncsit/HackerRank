
def average(arr):
	arr_set = set(arr)
	return sum(arr_set)/len(arr_set)

if __name__ == '__main__':
	n = int( input() )
	arr = list( map( int, input().split() ) )
	result = average(arr)
	print(result)