a  = int(input("Enter first number: "))
b  = int(input("Enter second number: "))

Min = lambda a,b: a if a<b else b
print(Min(a,b))