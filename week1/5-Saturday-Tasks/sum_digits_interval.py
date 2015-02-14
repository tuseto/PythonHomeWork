n = int(input("Enter number n: "))
m = int(input("Enter number m: "))
result_1=0
result=0
new_n = None

while n <= m:
    new_n = n
    result_1=0
    while new_n != 0:
        result = new_n % 10
        new_n = new_n // 10
        result_1+=result
    print("Sum of digits of {0} is {1}.".format(n,result_1))
    n+=1
    
    




