items_num, cap = map(int, input().split())

valuesweights = []
for i in range(items_num):
    v, w = map(int, input().split())
    valuesweights.append([v, w, v/w])
valuesweights.sort(key=lambda x: x[2], reverse=True)
# print(valuesweights)
rem_cap = cap
ans = 0
i = 0
total = 0
for j in range(items_num):
    total += valuesweights[j][1]

while rem_cap > 0 and total > 0:
    # print(i)
    if valuesweights[i][1] < rem_cap:
        ans += valuesweights[i][0]
        total -= valuesweights[i][1]
    else:
        ans += rem_cap*valuesweights[i][2]
    rem_cap = rem_cap - valuesweights[i][1]
    # print(rem_cap)
    # print(ans)
    i += 1
print("{:.4f}".format(ans))
