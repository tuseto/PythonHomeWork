n = int(input("enter number: "))
counter = 1

while counter < n:
    if n % counter == 0:
        print(counter)
    counter +=1
