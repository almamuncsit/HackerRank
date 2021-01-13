
# def sherlockAndAnagrams(s):
#     memo = {}
#     anagram_count = 0
#     for i in range(1, len(s)):
#         for j in range(len(s)-(i-1)):
#             key = ''.join(sorted(s[j:j+i]))
#             memo[key] = memo.get(key, 0) + 1
    
#     for item in memo.values():
#         anagram_count += item * (item-1)/2

#     return int(anagram_count)



def sherlockAndAnagrams(s):
    memo = {}
    anagram_count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            key = ''.join(sorted(s[i:j+1]))
            memo[key] = memo.get(key, 0) + 1
    
    for item in memo.values():
        anagram_count += item * (item-1)/2

    return int(anagram_count)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print(result)
