def printNumber(No):
    for i in range(1,No+1,1):
        print(i)

def main():
    No = int(input("Enter a number: "))
    printNumber(No)

if __name__=="__main__":
    main()