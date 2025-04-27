# Write your solution here

def transpose(matrix: list):
    trans_matrix = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            change = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = change
