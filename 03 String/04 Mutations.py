
def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    return ''.join(str_list)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
