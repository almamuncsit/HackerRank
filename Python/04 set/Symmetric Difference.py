if __name__ == '__main__':
	m = int( input() )
	m_set = set( input().split() )
	n = int( input() )
	n_set = set( input().split() )

	data_list = list(m_set.difference(n_set)) + list(n_set.difference(m_set));
	data_list = list( map(int, data_list) )
	data_list.sort(reverse=False)

	for item in range(0, len(data_list)):
		print( data_list[item] )