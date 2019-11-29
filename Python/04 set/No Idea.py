
def happiness(input_array, A, B):
	happiness_score = 0
	for i in input_array:
		if i in A:
			happiness_score += 1
		if i in B:
			happiness_score -= 1
	return happiness_score


def main():
	n, m = input().split()
	input_array = list( map( int, input().split() ) )
	A = set( map( int, input().split() ) )
	B = set( map( int, input().split() ) )
	print( happiness( input_array, A, B ) )


if __name__ == '__main__':
	main()