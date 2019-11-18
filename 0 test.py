def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


# Driver Code
sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
sorted_list = Sort(sub_li)
print(sorted_list.pop())
print(sorted_list)
