n = int(input())
english = set( map( int, input().split() ) )

p = int(input())
franch = set( map( int, input().split() ) )
new_set = english.symmetric_difference(franch)
print( len(new_set) )