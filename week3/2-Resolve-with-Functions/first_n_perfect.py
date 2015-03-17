def is_perfect(num):
    array = []
    for i in range(1,num-1):
        if num % i == 0:
            array += [i]
    if sum_ints(array) == num:
        return(num)
    else:
        return(False)


def sum_ints(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def first_perfect(n):
    counter = 1
    moment_number = 1
    result = []
    while counter <= n:
        moment_number += 1
        if is_perfect(moment_number):
            result += [moment_number]
            counter += 1
    return (result)
            

n = int(input("Enter n: "))
print (first_perfect(n))
