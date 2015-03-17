n = int(input("Enter number: "))
counter = 2
prime = True
<<<<<<< HEAD
a = 0
b = 0
=======

>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
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
<<<<<<< HEAD
    print(str(n) + " is prime")
    a = n - 2
    
    while counter < a:
        if n % counter != 0:
            counter+=1
            prime = True
        elif n % counter == 0:
            prime = False
            break
    if prime:
        print(str(a) + " is prime")
        b = n + 2
    
    while counter < a:
        if n % counter != 0:
            counter+=1
            prime = True
        elif n % counter == 0:
            prime = False
            break
    if prime:
        print(str(b) + " is prime")
    
=======
    print("is prime")
>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
else:
    print("is not prime")
        

            
    
    
