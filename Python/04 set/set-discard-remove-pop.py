
n = int(input())
s = set( map(int, input().split()) )
N = int( input() )

for i in range(0,N):
	input_data = input().split()
	if input_data[0] == 'pop':
		s.pop()
	if input_data[0] == 'remove':
		s.remove( int(input_data[1]) )
	if input_data[0] == 'discard':
		s.discard( int(input_data[1]) )

print(sum(s))
		