def board_to_string(board):
    tictac = ""
    for el in board:
        tictac += "|"+" "
        for el2 in el:
            tictac = tictac + el2 +" "+ "|"+" " 
        tictac += "\n"
    return(tictac)




board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string(board)
print(result)