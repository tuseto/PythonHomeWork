def is_prime(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    return(is_prime)

def twins(n):
    first_twin = n - 2
    second_twin = n + 2
    if is_prime(n) == True:
        print(str(n) + " is prime")
        if is_prime(first_twin) == True:
            print(str(first_twin) + " is prime")
        else:
            print(str(first_twin) + " is not prime")
        if is_prime(second_twin) == True:
            print(str(second_twin) + " is prime")
        else:
            print(str(second_twin) + " is not prime")
    else:
        print(str(n) + " is not prime")

n = int(input("Enter n: "))
print(twins(n))
