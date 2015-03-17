n = int(input("Enter n: "))

digits = []
number = 0

while n != 0:
    number = n % 10
    n = n // 10
    digits = [number] + digits 
print(digits)

number = 0

for num in digits:
    number = number * 10 + num
print(number)
    

