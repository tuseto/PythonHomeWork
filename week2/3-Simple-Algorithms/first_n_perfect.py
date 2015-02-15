perf_numbers = int(input("enter number: "))

counter = 1

number = 1
divider = 0

sum_dividers = 0


while counter <= perf_numbers:
        while divider < number:
            if number % divider == 0:
                sum_dividers += divider
                if sum_dividers == number:
                    counter += 1
                    print(number)
            divider += 1
number += 1
    

