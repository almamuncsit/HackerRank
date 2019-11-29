if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr = sorted(arr, key=int, reverse=True)
    arr.pop(0)
    print(arr.pop(0))
