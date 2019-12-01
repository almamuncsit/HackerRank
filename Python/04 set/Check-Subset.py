
T = int( input() )
for x in range(0,T):
	n = int(input())
	A = set(input().split())
	m = int(input())
	B = set(input().split())
	
	if len(A.difference(B)):
		print('False')
	else:
		print('True')