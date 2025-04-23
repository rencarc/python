# Write your solution here
def who_won(game_board: list):
    play1 = 0
    play2 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                play1 += 1
            elif square == 2:
                play2 += 1
                     
                     

    if play1 > play2:
        return 1
    elif play1 < play2:
        return 2
    elif play1 == play2:
        return 0
