def to_digits(n):
    digits = []
    while n != 0:
        digits += [n % 10]
        n = n // 10
    return (digits)

def is_prime(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    return(is_prime)

def check(digits):
    prime_digit = False
    for el in digits:
        if is_prime(el) == True:
            prime_digit = True
            break
    if prime_digit:
        return("Yes there is prime digit")
    else:
        return("There isnt prime digit")
        
        
    
n = int(input("Enter n: "))
print (check(to_digits(n)))
