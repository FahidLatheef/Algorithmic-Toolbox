def binary_search(array, start, end, to_find):
    mid = start + (end - 1 - start) // 2
    if array[0] == to_find:
        return 0
    if array[-1] == to_find:
        return len(array)-1

    if start == end:
        if to_find == array[mid]:
            return mid
        else:
            return -1
    else:
        if to_find > array[mid]:
            start = mid
            return binary_search(array, start + 1, end, to_find)
        elif to_find < array[mid]:
            end = mid
            return binary_search(array, start, end, to_find)
        else:
            return mid


data = list(map(int, input().split()))
n = data[0]
a = data[1: n + 1]
check_list = list(map(int, input().split()))
for x in check_list[1:]:
    if x < a[0] or x > a[n - 1]:
        print(-1, end=" ")
    else:
        print(binary_search(a, 0, n, x), end=" ")
