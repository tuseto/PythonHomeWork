number = int(input("Enter number: "))

first_number = number % 10
number = number // 10

second_number = number % 10
number = number // 10

third_number = number % 10

print(first_number)
print(second_number)
print(third_number)

if first_number < second_number > third_number:
    if first_number < third_number:
        print(second_number*100 + third_number*10 +first_number)
    else:
        print(second_number*100 + first_number*10 +third_number)

if first_number < third_number > second_number:
    if first_number < second_number:
        print(third_number*100 + second_number*10 + first_number)
    else:
        print(third_number*100 + first_number*10 + second_number)

if second_number < first_number > third_number:
    if second_number < third_number:
        print(first_number*100 + third_number*10 + second_number)
    else:
        print(first_number*100 + second_number*10 + third_number)

    







