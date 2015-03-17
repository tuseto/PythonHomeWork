def digits(n):
    digits = []
    while n != 0:
        digits += [n % 10]
        n = n // 10
    return (digits)

def smallest_number(digits):
    digits = sorted(digits)
    return(digits)

def biggest_number(digits):
    digits = sorted(digits, reverse = True)
    return(digits)

def list_to_number(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    return (number)
        
def result(n):
    print("Smallest number is: " + str(list_to_number(smallest_number(digits(n)))))
    print("Biggest number is: " + str(list_to_number(biggest_number(digits(n)))))
    return("")
    
n = int(input("Enter n: "))
print (result(n))

