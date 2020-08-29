def majority_element(lis):
    max_counter = 0
    prev_element = -1  # Initialising
    current_counter = 0
    for ele in lis:
        if ele == prev_element:
            current_counter += 1
            prev_element = ele
        else:
            prev_element = ele
            current_counter = 1

        if current_counter > max_counter:
            max_counter = current_counter

        if (max_counter > len(lis)//2) or (current_counter > len(lis)//2):
            return 1
    return 0

int(input())
a = list(map(int, input().split()))
print(majority_element(sorted(a)))
