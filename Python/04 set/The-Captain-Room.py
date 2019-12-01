
def coptain_room(rooms, k):
	myset = set(rooms)
	ans = (sum(myset)*k) - sum(rooms)
	return (ans // (k-1))


if __name__ == '__main__':
	k = int( input() )
	rooms = list(map(int, input().split()))
	print(coptain_room(rooms, k))

