n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
even_numbers = []

while count <= n:
    number = int(input("Enter number: "))
    
    numbers = numbers + [number]

    count += 1

    if number % 2 == 0:
        even_numbers = even_numbers + [number]
print("Count of evens: " + str(len(even_numbers)))
print("Evens are: ")
for number in even_numbers:
    print(number)

