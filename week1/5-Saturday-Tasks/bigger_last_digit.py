n=int(input("Enter number n: "))
m=int(input("Enter number m: "))

n_left = n % 10
m_left = m % 10

if n_left > m_left:
    print(str(n)+" last number is bigger")
elif n_left < m_left:
    print(str(m)+" last number Is bigger")
else:
    if n > m:
        print(str(n)+"  is bigger")
    else:
        print(str(m)+"  Is bigger")
