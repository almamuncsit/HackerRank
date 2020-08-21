def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i*r in dictPairs:
            count += dictPairs[i*r]
        if i*r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        dict[i] = dict.get(i, 0) + 1

    return count


# def countTriplets(arr, r):
#     arr_dict = {}
#     tripletsCount = 0
#     arr = list(map(int, arr))
    
#     for item in arr:
#         arr_dict[item] = arr_dict.get(item, 0) + 1

#     for item in arr:
#         second = item * r
#         third = second * r
#         if second in arr_dict and third in arr_dict:
#             tripletsCount += arr_dict[second] * arr_dict[third]

#     return tripletsCount


if __name__ == '__main__':
    nr = input().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = input().split()
    arr = list(map(int, arr))
    resutl = countTriplets(arr, r)
    print(resutl)
