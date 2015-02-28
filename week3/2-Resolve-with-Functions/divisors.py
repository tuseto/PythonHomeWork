def divisors(n):
    divider = 1
    array = []
    while divider < n:
        if n % divider == 0:
            array += [divider]
        divider += 1
    return array

n = int(input("Enter n: "))
print(divisors(n))
