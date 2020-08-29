"""import random


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a


def partition3(a, l, r):
    if l >= r:
        return a
    left_index = 0
    centre_index = 0
    right_index = 0
    k = random.randint(l, r)  # Pivot
    swap(a, k, r)  # Swapping pivot and the last element
    for i in range(l, r):
        if a[i] < a[r]:
            swap(a, i, left_index)
            left_index += 1
        elif a[i] == a[r]:
            swap(a, i, left_index + centre_index)
            centre_index += 1
        elif a[i] > a[r]:
            swap(a, i, left_index + centre_index + right_index)
            right_index += 1
    a = a[:left_index] + a[left_index + right_index:] + a[left_index:left_index + right_index]
    return a

def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition3(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

lis = [7, 2, 3, 1, 9, 2, 6, 2, 6]
print(partition3(lis, 0, 8))
"""
import random


def partition(arr, pivot):
    less, equal, greater = [], [], []
    for val in arr:
        if val < pivot:
            less.append(val)
        if val == pivot:
            equal.append(val)
        if val > pivot:
            greater.append(val)
    return less, equal, greater


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    less, equal, greater = partition(arr, pivot)
    return qsort(less) + equal + qsort(greater)


int(input())
array = list(map(int, input().split()))
for x in qsort(array):
    print(x, end=" ")
