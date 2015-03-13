from random import randint


def generate_random_list(n, start, end):
    counter = 1
    number_array = []    
    while counter <= n:
        number_array += [randint(start, end)]
        counter += 1
    return(number_array)

n = int(input("Enter num of elements: "))
start = int(input("Enter lower bound of elements: "))
end = int(input("Enter upper bound of elements: "))
print(generate_random_list(n,start,end))        
