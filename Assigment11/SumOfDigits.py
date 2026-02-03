def Sum(No):
    s = 0
    while No>0:
        Digit = No%10
        s+=Digit
        No=No//10
    print(s)

def main():
    No = int(input("Enter value: "))
    Sum(No)

if __name__=="__main__":
    main()