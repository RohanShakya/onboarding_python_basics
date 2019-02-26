import math
c = 50
h = 30
d = input("Enter few numbers in comma separated sequence: ")
x = d.split(",")
print(x)

print("The result is: ")
for i in x:
    q = math.sqrt((2*c*int(i))/h)
    q1 = round(q)
    print(q1, end=",")


