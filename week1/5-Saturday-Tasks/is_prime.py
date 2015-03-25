n = int(input("Enter number: "))
counter = 2
prime = True
if n != 1:
    while counter < n:
        if n % counter != 0:
            counter+=1
            prime = True
        elif n % counter == 0:
            prime = False
            break
else:
    prime = False
if prime:
    print(str(n) + " is prime")
else:
    print("is not prime")

