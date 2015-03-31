def string_matrix(matrix_width,strings):
    matrix = ""
    for i in range(0,matrix_width):
        matrix += "| "
        if i >= len(strings):
            for r in range(0,matrix_width):
                matrix += "X" + " | "
        else:
            for n in range(0,matrix_width):
                if n >= len(strings[i]):
                    matrix += "X" + " | "
                else:
                    matrix += strings[i][n] + " | "
        matrix += "\n"
    return(matrix)



print(string_matrix(2,["python","gogo","perl","java","haskell","ruby0nRails"]))
