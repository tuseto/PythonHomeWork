def loss_or_profit(income,outcome):
    profit = 0
    loss = 0
    for el in income:
        profit += el
    for el in outcome:
        loss += el
    result = profit - loss
    if result > 0:
        return("+" + str(result))
    elif result < 0:
        return(result)
    else:
        return("=" + str(result))
print (loss_or_profit([10], [10]))