def palindrome(No):
    OriginalNumber = No
    rev = 0
    while No>0:
        Digit = No%10
        rev = rev*10+Digit
        No = No//10
    if rev ==OriginalNumber:
        print("It is a palindrome number")
    else:
        print("Not a palindrome number")

def main():
    No = int(input("Enter a number: "))
    palindrome(No)

if __name__=="__main__":
    main()