def square(x):
    return x**2


def fact(x):
    counter = 1
    result = 1
    while counter <= x:
        result *= counter
        counter += 1
    return result


def count_elements(items):
    items_number = 0
    for el in items:
        items_number += 1
    return items_number


def member(x,xs):
    element = 0
    while element <= len(xs)-1:
        if x == xs[element]:
            return True
        else:
            return False


def grades_that_pass(students,grades,limit):
    lenght = len(students)
    passed = []
    for i in range(0,lenght):
        if grades[i] >= limit:
            passed += [students[i]]
    return passed

       
