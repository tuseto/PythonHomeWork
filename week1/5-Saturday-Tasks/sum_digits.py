n=int(input("Enter number n: "))
result=0

while n != 0:
    digit = n % 10
    n = n // 10
    result+=digit
print(result)
       
