from collections import deque

d = deque()

for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)
[print(x, end=' ') for x in d]
