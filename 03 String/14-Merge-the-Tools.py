
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
    	unique_list = []
    	str_list = list(string[i:i+k])
    	for c in str_list:
    		if c not in unique_list:
    			unique_list.append(c)
    	print("".join(unique_list))


if __name__ == '__main__':
	string, k = input(), int( input() )
	merge_the_tools(string, k)
	
