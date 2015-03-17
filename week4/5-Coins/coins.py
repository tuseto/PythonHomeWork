# Coins: 1,2,100,5,10,50,20

def calculate_coins(sum):
    arr = {}
    coins = [100,50,20,10,5,2,1]
    
    sum = round(sum * 100)

    for coin in coins:
        res = sum // coin
        arr[coin] = res
        sum = sum - res * coin
    
    return arr

print(calculate_coins(8.54))


