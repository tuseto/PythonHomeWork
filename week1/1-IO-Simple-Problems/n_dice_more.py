from random import randint

N=int(input('Enter dice sides: '))

result1=randint(1,N)
result2=randint(1,N)
result3=randint(1,N)

print("Your 1 throw: "+str(result1))
print("Your 2 throw: "+str(result2))
print("You 3 throw: "+str(result3))
print("Sum of throws: "+str(result1+result2+result3))
