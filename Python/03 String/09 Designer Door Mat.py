
if __name__ == '__main__':
    symbol = '.|.'
    a, b = input().split()
    a = int(a)
    b = int(b)
    center = int(a / 2)+1
    length = 1
    for i in range(1, a+1):
        if i < center:
            print((symbol*length).center(b, '-'))
            length += 2
        elif i > center:
            print((symbol*length).center(b, '-'))
            length -= 2
        else:
            print("WELCOME".center(b, '-'))
            length -= 2
