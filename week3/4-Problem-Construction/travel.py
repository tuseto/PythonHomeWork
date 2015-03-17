
def travel_cost(travels):
    price = 0
    tickets = 0
    
    for el in travels:
        if el < 23:
            price += el
        else:
            price += 23
        if price > 50:
            price = 50
    return(price)

    
print(travel_cost([22]))


            
