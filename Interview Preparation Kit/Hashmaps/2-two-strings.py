
def twoStrings(s1, s2):
    s1_dic = {}

    for c in s1:
        s1_dic[c] = 1

    for c in s2:
        if c in s1_dic:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)
