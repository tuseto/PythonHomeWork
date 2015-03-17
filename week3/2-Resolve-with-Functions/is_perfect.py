def is_perfect(n):
    array = []
    for i in range(1,n-1):
        if n % i == 0:
            array += [i]
    if sum_ints(array) == n:
        return("Its perfect")
    else:
        return("Its not")


def sum_ints(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

n = int(input("Enter n: "))
print (is_perfect(n))
