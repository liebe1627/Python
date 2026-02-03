def check(No):
    if No > 0:
        print("Positive number")
    elif No<0:
        print("Negative number")
    else:
        print("Zero")

def main():
    No = int(input("Enter a number: "))
    check(No)

if __name__ == "__main__":
    main()