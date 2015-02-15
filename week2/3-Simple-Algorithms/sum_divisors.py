n = int(input("enter number: "))
counter = 1
result = 0
while counter < n:
    if n % counter == 0:
        result += counter
    counter +=1
print(result)
