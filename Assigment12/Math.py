def Addition(A,B):
    Sum = 0
    Sum = A+B
    print("The addition is", Sum)

def Subtraction(A,B):
    Sub = 0
    Sub = A-B
    print("The addition is", Sub)

def Multiplication(A,B):
    Mult = 0
    Mult = A*B
    print("The addition is", Mult)

def Division(A,B):
    Div = 0
    Div = A/B
    print("The addition is", Div)

def main():
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))
    Addition(A,B)
    Subtraction(A,B)
    Multiplication(A,B)
    Division(A,B)

if __name__ == "__main__":
    main()
