n = int(input())
A = set( map( int, input().split() ) )
n = int(input())
for i in range(0, n):
	operetions = input().split()
	another_set = set( map( int, input().split() ) )
	if operetions[0] == 'intersection_update':
		A.intersection_update(another_set)
	if operetions[0] == 'update':
		A.update(another_set)
	if operetions[0] == 'symmetric_difference_update':
		A.symmetric_difference_update(another_set)
	if operetions[0] == 'difference_update':
		A.difference_update(another_set)

print(sum(A))
