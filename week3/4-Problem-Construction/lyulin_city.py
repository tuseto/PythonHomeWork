num_of_mansions = int(input("Enter num of mansions: "))
mansion_height = []

for i in range(0,num_of_mansions):
    mansion_height += [int(input("Enter mansion height: "))]

def result(masion_height):
    if len(mansion_height) == 0:
        return(0)
    counter = 1
    equal = mansion_height[0]
    for el in mansion_height:
        if equal < el:
            equal = el
            counter += 1
    return(counter)
       
print(result(mansion_height))

