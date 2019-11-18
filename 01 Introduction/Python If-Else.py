if __name__ == '__main__':
    n = int(input())
    mod = n % 2

    if mod == 1:
        print('Weird')

    elif 2 <= n <= 5:
        print('Not Weird')

    elif 6 <= n <= 20:
        print('Weird')

    elif n > 20:
        print('Not Weird')
