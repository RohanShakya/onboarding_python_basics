def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

inp = input("Enter a number: ")
inpu = int(inp)

print("factorial=", fact(inpu))