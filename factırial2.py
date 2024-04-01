def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

while True:
    try:
        number = int(input("number = "))
        if number < 0:
            print("Number must be positive.")
        else:
            print(f"{number}! = {fac(number)}")
    except ValueError:
        print("There is an error")
