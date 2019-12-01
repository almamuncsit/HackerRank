n = int(input())
english = set( map( int, input().split() ) )

p = int(input())
franch = set( map( int, input().split() ) )
new_set = english.union(franch)
print( len(new_set) )