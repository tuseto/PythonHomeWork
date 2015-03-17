n = int(input("Enter n: "))

count = 1
numbers = []
result = 0

while count <= n:
    number = int(input("Enter number: "))
    numbers = numbers + [number]
    count += 1
    
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    
    
print(max_num)
    

    

   



