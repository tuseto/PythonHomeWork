from random import randint

dice = 5
dice_sides = 6



counter = 0
throw = 0
result = 0


i_player_score = 1001
m_player_score = 1001

while True:
    counter = 0
    throw = 0
    result=0
    if m_player_score == 0:
        print("Mariq WON")
        break
    elif i_player_score == 0:
        print("Ivan WON!")
        break
    while counter <= 5:
        throw = randint(1,dice_sides)
        result = result + throw
        counter = counter + 1
        print("Ivan Throw: "+str(throw))
    print("Sum of Ivan throws: "+str(result))
    if i_player_score > 0:
        i_player_score = i_player_score - result
    elif i_player_score < 0:
        i_player_score = i_player_score + result
    print("Ivan`s score: " + str(i_player_score))

    counter = 0
    throw = 0
    result=0
    while counter <= 5:
        throw = randint(1,dice_sides)
        result = result + throw
        counter = counter + 1
        print("Mariq Throw: "+str(throw))
    print("Sum of Mariq throws: "+str(result))
    if m_player_score > 0:
        m_player_score = m_player_score - result
    elif m_player_score < 0:
        m_player_score = m_player_score + result
   
    print("Mariq`s score: " + str(m_player_score))



   
