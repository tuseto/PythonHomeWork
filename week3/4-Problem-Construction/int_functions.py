def reverse_int(n):
    reversed_number = 0
    while n != 0:
        reversed_number = reversed_number*10 + n % 10
        n = n // 10
    return (reversed_number)

def sum_digits(n):
    sum_digits = 0
    while n != 0:
        sum_digits += n % 10
        n = n // 10
    return (sum_digits)

def product_digits(n):
    multi_digits = 1
    while n != 0:
        multi_digits *= n % 10
        n = n // 10
    return (multi_digits)
    
        
n = int(input("Enter n: "))
print("Reversed:")
print(reverse_int(n))
print("Sum:")
print(sum_digits(n))
print("Multiplication:")
print(product_digits(n))
        
    
