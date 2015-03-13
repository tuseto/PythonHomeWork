def prime_pair(numbers):
    for num in numbers:
        for num2 in numbers:
            result = num + num2
            if is_prime(result):
                return True
    return False

def is_prime(num):
    is_prime = True
    if num <= 1:
        is_prime = False
    elif num == 2:
        is_prime = True
    else:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
    return is_prime

print(prime_pair([2,2,3]))



