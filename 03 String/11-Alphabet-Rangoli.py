import string

def prnt_rangoli(size):
	alpha = string.ascii_lowercase
	l = []
	for i in range(0, size):
		s = "-".join( alpha[i:size] )
		l.append( (s[::-1] + s[1:]).center(4*n-3, '-') )
	print( '\n'.join(l[::-1] + l[1:]) )


if __name__ == '__main__':
	n = int( input() )
	prnt_rangoli(n)