n = int(input("enter number: "))
counter = 1
number = 1
devider = 1
result = 0

while counter <= n:
    while True:
        number += 1
        devider = 1
        result = 0
        while devider < number:
            if number % devider == 0:
                result += devider
            devider += 1    
        if result == number:
            counter += 1
            print(number)
            break
    
    


