# Write your solution here
def row_sums(my_matrix: list):
    for row in my_matrix:
        total = sum(row)
        new_row = row.append(total)   
