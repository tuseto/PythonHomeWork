input_number = int(input("Enter number: "))
result = ""
digit = 0
n = input_number
while n != 0:
    digit = n % 10
    n = n // 10
    number = str(digit) 
    result = result + number

result = int(result)
if input_number == result:
    print(str(input_number)+" is palindrom")
else:
    print(str(input_number)+" is NOT palindrom")
