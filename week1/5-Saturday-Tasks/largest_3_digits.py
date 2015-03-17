<<<<<<< HEAD
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

=======
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

number = a*100 + b*10 + c
print(number)
>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
    




<<<<<<< HEAD



=======
>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
