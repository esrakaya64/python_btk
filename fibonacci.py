def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
while True:
    value=int(input("Number of element: "))
    for i in range(1, value):
        print(fib(i) , end="..")
    print()