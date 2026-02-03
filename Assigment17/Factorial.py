def factorial(No):
    sum = 1
    for i in range(1,No+1):
        sum = sum*i
    print(sum)

def main():
    No = int(input("Enter a number: "))
    factorial(No)

if __name__=="__main__":
    main()        
