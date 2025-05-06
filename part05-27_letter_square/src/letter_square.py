def letter_square(levels: int):

    size = levels * 2 - 1  
    matrix = [[""] * size for _ in range(size)] 


    for i in range(levels):
        char = chr(ord('A') + levels - i - 1) 
        for j in range(i, size - i):
            matrix[i][j] = char
            matrix[size - i - 1][j] = char 
            matrix[j][i] = char 
            matrix[j][size - i - 1] = char  

    for row in matrix:
        print("".join(row))



