a=int(input("Enter a: "))
b=int(input("Enter b: "))
counter = a

while counter <= b:
    if counter%2==0:
        print(str(counter)+" - even")
    else:
        print(str(counter)+" - odd")
    counter+=1
    
while a >= b:
    if b%2==0:
        print(str(b)+" - even")
    else:
        print(str(b)+" - odd")
    b+=1


    
