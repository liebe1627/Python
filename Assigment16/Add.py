def Add(a,b):
    return a+b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    A = Add(a,b)
    print("The addition is: ",A)

if __name__=="__main__":
    main()
