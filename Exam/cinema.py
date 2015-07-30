def order_of_seats(cinema):
    row_counter = 0         #Брояч на редовете
    column_counter = 0      #Брояч на колоните
    unordered_free_seats = []   #Лист за свободните места подред (от начало до край)
    empty_seats_arr = []    #Лист с tuples за брой свободни места на всеки ред

    #Цикъл обхождащ редовете
    for row in cinema:
        row_counter += 1
        column_counter = 0
        empty_seats_counter = 0

        #Цикъл обхождащ колоните
        for column in row:
            column_counter += 1
            if column == 0:
                empty_seats_counter += 1
                unordered_free_seats += [(row_counter,column_counter)] #Броячите се прибавят (ред,колона)

        #Пропускат се пълните редове. За останалите редове се записват (номер ред - брой празни места)
        if empty_seats_counter != 0:
            empty_seats_arr +=[(row_counter,empty_seats_counter )]

    #Функция за сортиране на празните места за всеки номер ред, като се започва от най-малкият брой празни места
    sorted_empty_seats = sort_empty_seats(empty_seats_arr)

    #Функция сортираща неподредените места чрез сортирания лист с (номер ред - празни мяста)
    final_result = order_by_empty_seat(unordered_free_seats,sorted_empty_seats)

    return(final_result)


def sort_empty_seats(empty_seats_arr):
    sorted_empty_seats = sorted(empty_seats_arr, key=lambda tup: tup[1])
    return(sorted_empty_seats)

def order_by_empty_seat(unordered_free_seats,sorted_empty_seats):
    final_result = []
    for el in sorted_empty_seats:
        for el1 in unordered_free_seats:
            if el[0] == el1[0]:        #Сравняват се номерата на редовете от 2-та списъка
                final_result += [el1]
    return(final_result)


cinema = [ [1, 0, 0],
           [0, 1, 0],
           [0, 0, 1, 1] ]


print (order_of_seats(cinema))









