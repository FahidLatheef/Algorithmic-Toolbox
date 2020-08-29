n = int(input())

sequence = {1: [1],
            2: [1, 2],
            3: [1, 3],
            4: [1, 3, 4],
            5: [1, 3, 4, 5]}

for i in range(6, n + 1, 1):
    first, second, third = 10e50, 10e50, 10e50
    if i % 3 == 0:
        first = len(sequence[i // 3])

    if i % 2 == 0:
        second = len(sequence[i // 2])

    third = len(sequence[i - 1])

    if min(first, second, third) == first:
        temp = sequence.get(i // 3)
        temp2 = temp.copy()  # This copying is vital
        temp2.append(i)
        sequence[i] = temp2
    elif min(first, second, third) == second:
        temp = sequence[i // 2]
        temp2 = temp.copy()
        temp2.append(i)
        sequence[i] = temp2
    else:
        temp = sequence[i - 1]
        temp2 = temp.copy()
        temp2.append(i)
        sequence[i] = temp2

print(len(sequence[n]) - 1)
for x in sequence[n]:
    print(x, end=' ')
