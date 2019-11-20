
def split_and_join(line):
    str_arr = line.split(" ")
    return "-".join(str_arr)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
