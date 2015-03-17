n = int(input("Enter n: "))

count = 1
numbers = []
result = 0

while count <= n:
    number = int(input("Enter number: "))
    numbers = numbers + [number]
    count += 1

sum_result = 0
counter = 0

for num in numbers:
    sum_result += num
    counter += 1
average = sum_result / counter
print(average)

    
    

    

    

   





