#  I tried manually doing it and observed the recurring pattern
def get_change(m):
    if m == 2:
        return 2
    else:
        return (m+3)//4


m = int(input())
print(get_change(m))
