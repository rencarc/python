def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no] 
    numbers = [num for num in row if num > 0]  
    return len(numbers) == len(set(numbers)) 



