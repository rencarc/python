
def sudoku_grid_correct(sudoku: list) -> bool:

    for row_no in range(9):
        if not sudoku_grid_correct(sudoku, row_no):
            return False


    for column_no in range(9):
        if not sudoku_grid_correct(sudoku, column_no):
            return False


    for row_start in range(0, 9, 3): 
        for column_start in range(0, 9, 3): 
            if not sudoku_grid_correct(sudoku, row_start, column_start):
                return False


    return True