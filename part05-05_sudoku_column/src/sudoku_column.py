def column_correct(sudoku: list, column_no: int) -> bool:

    column = [sudoku[row][column_no] for row in range(len(sudoku))]

    numbers = [num for num in column if num > 0]
    return len(numbers) == len(set(numbers))
