def factorial(No1):
    sum = 1
    for i in range(1,No1+1,1):
        sum *= i
    print("The factorial is: ",sum)

def main():
    No1 = int(input("Enter a number: "))
    factorial(No1)

if __name__=="__main__":
    main()