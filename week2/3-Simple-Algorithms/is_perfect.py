n = int(input("enter number: "))
counter = 1
result = 0
while counter < n:
    if n % counter == 0:
        result += counter
    counter +=1
if result == n:
    print("Number is perfect")
else:
    print("Number is not perfect")
<<<<<<< HEAD
    


=======
>>>>>>> bc47b4ee840a28662cd717c01ffdfc44881442f1
