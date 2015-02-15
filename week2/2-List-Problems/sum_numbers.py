n = int(input("Enter n: "))

count = 1
numbers = []
result = 0
while count <= n:
    number = int(input("Enter number: "))
    numbers = numbers + [number]
    count += 1
for num in numbers:
    result = result + num
print("The sum is: " + str(result))
    

   



