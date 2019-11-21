
def minion_game(string):
	vowels = 'AEIOU';
	keysc = 0
	stusc = 0
	for i in range( 0, len(string) ):
		if string[i] in vowels:
			keysc += len(string) - i
		else:
			stusc += len(string) - i

	if keysc > stusc:
		print('Kevin {}'.format(keysc))
	elif stusc > keysc:
		print( 'Stuart {}'.format(stusc) )
	else:
		print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)