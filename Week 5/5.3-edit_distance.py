def edit_distance(s, t):
    matrix = [[0 for col in range(len(t) + 1)] for row in range(len(s) + 1)]  # opposite
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                if s[i - 1] is t[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                elif s[i - 1] is not t[j - 1]:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
    # return matrix # for visualizing
    return matrix[-1][-1]  # returns last element


#  import numpy

# print(numpy.array(edit_distance(input(), input())))  # For visualising
print(edit_distance(input(), input()))
