def Reverse(No): 
    rev = 0
    while No>0:
        Digit = No%10
        rev = rev*10+Digit
        No = No//10
    print(rev)

def main():
    No = int(input("Enter the number: "))
    Reverse(No)

if __name__=="__main__":
    main()