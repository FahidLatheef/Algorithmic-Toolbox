def is_greater_or_equal(a, b):
    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        return True
    else:
        return False


def largest_number(num_list):
    answer = []
    lis = num_list
    while len(lis) != 0:
        maxnum = 0
        for num in lis:
            if is_greater_or_equal(num, maxnum):
                maxnum = num
        answer.append(maxnum)
        try:
            lis.remove(maxnum)
        except ValueError:
            continue
    return answer


_ = int(input())
a = list(map(int, input().split()))
an = largest_number(a) # calling the fn
ane = [str(i) for i in an] # converting them to string
print("".join(ane)) # joining the strings
