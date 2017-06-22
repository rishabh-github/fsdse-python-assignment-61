def solution(list_of_nums):
    dic = {}
    even = 0
    odd = 0

    for num in list_of_nums:
        if num%2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    dic.update({'EVEN':even})
    dic.update({'ODD':odd})

    return dic

print solution([1, 2, 3, 5, 8, 9])
