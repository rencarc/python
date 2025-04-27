# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:

    sudoku_copy = [row[:] for row in sudoku]

    if 1 <= number <= 9:
        sudoku_copy[row_no][column_no] = number
    return sudoku_copy 

def print_sudoku(sudoku: list):

    for row in sudoku:
        row_output = []
        for number in row:
            if number == 0:
                row_output.append("_")
            else:
                row_output.append(str(number))
        print(" ".join(row_output))

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)  
    print("Original:")
    print_sudoku(sudoku) 
    print()
    print("Copy:")
    print_sudoku(grid_copy)  
