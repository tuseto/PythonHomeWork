def magic_square(square):
    rows = []
    column = []
    main_diagonal = []
    second_diagonal = []
    
#Sum of rows
    for row in square:
        summ = 0
        for i in range(0, len(row)):
            summ += row[i]
        rows += [summ]
        
#Sum of columns        
    for i in range(0, len(square[0])):
        summ = 0
        for row in square:
            summ += row[i]    
        column += [summ]
                    
#Sum of main_diagonal
    counter = 0
    summ = 0
    for row in square:      
        summ += row[counter]    
        counter += 1
    main_diagonal += [summ]

#Sum of second_diagonal
    counter = len(square[0])-1
    summ = 0
    for row in square:    
        summ += row[counter]
        counter -= 1
    second_diagonal += [summ]

    arr = rows + column + main_diagonal + second_diagonal
    
    for i in range(0, len(arr)):
        if arr[0] != arr[i]:
            return False
        
    return True
        
        
print(magic_square([ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]))
