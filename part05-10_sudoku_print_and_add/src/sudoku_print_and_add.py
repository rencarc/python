# Write your solution here
def print_sudoku(sudoku: list):
 for row in sudoku:

        row_output = []
        for number in row:
            if number == 0:
                row_output.append("_")
            else:
                row_output.append(str(number)) 

        print(" ".join(row_output))





def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    if 1 <= number <= 9:
        sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 7, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 7, 0, 3, 0, 0, 0],
        [0, 0, 4, 0, 7, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print_sudoku(sudoku) 
    print()

    add_number(sudoku, 0, 3, 5)
    add_number(sudoku, 1, 6, 4)
    add_number(sudoku, 2, 8, 1)

    print("Three numbers added:")
    print()
    print_sudoku(sudoku) 

    