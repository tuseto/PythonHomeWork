def divisors(n):
    divider = 1
    array = []
    while divider < n:
        if n % divider == 0:
            array += [divider]
        divider += 1
    return array

def sum_ints(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

n = int(input("Enter n: "))
print(sum_ints(divisors(n)))
