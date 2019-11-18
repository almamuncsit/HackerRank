if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(0, N):
        input_str = input()
        l = input_str.split()
        if l[0] == 'insert':
            my_list.insert(int(l[1]), int(l[2]))
        elif l[0] == 'print':
            print(my_list)
        elif l[0] == 'remove':
            my_list.remove(int(l[1]))
        elif l[0] == 'append':
            my_list.append(int(l[1]))
        elif l[0] == 'sort':
            my_list.sort()
        elif l[0] == 'pop':
            my_list.pop()
        elif l[0] == 'reverse':
            my_list.reverse()
