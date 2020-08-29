# 1 5 10
def get_change(m):
    count1, rem1 = m//10, m%10
    count2, rem2 = rem1//5, rem1%5
    return count1 + count2 +rem2


m = int(input())
print(get_change(m))
