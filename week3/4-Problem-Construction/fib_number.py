
def fib_number(n):
    counter = 1
    array = []
    next_el = 1
    result = 1
    first_el = 1

    if n == 1:
        array += [first_el]
    elif n == 2:
        array += [first_el, next_el]
    else:
        array += [first_el, next_el]        
        while counter <= n - 2:
        
            next_el = result
            result = next_el + first_el
            first_el = next_el

            array += [result]
            counter += 1
    return(array)

def to_number(array):
    result = ""
    for el in array:
        result += str(el)
    result = int(result)
    return(result)

n = int(input("Enter n: "))
print(to_number(fib_number(n)))
    
    
