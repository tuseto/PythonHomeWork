n = int(input("enter number: "))

digits = []
while n != 0:
    digit = n % 10
    digits = digits + [digit]
    n = n // 10
for digit in digits:
    if digit in [2,3,5,7]:
        print("theres prime")
        break
    else:
        print("theres no prime")
