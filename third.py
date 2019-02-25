inp = input("Enter a number: ")
n = int(inp)

mydict = {}

for i in range(1, n+1):
    mydict[i] = i*i

print(mydict)
