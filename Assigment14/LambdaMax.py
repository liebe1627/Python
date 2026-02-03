a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

Max = lambda a,b:a if a>b else b
print(Max(a,b))