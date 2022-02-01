n = int(input("How many terms of the Fibonacci series do you want: "))

n1 = 0
n2 = 1
i = 0

if n <= 0:
        print("Enter a positive no.")
elif n == 1:
    print("The Fibonacci sequence of numbers up to", n, ":",(n1))
else:
    print(" The fibonacci sequence is :")
    while i < n:
        print(n1)
        q = n1 + n2
        n1 = n2
        n2 = q
        i += 1
    
    




