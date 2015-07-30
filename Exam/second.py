def second_largest(numbers):

    if len(numbers) < 2:
        return False

    first_largest = max(numbers)
    numbers.remove(first_largest)
    sec_largest = max(numbers)

    while first_largest == sec_largest:
        if len(numbers) == 1:
            return False
        numbers.remove(sec_largest)
        sec_largest = max(numbers)

    return(sec_largest)


print(second_largest([7,1,2,3,4,5,5,6]))

