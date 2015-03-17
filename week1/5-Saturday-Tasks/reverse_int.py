n = int(input("Enter number: "))
result = ""
digit = 0

while n != 0:
    digit = n % 10
    n = n // 10
    number = str(digit) 
    result = result + number
    
print(result)




