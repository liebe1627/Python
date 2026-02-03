def grade(No):
    if No >= 75:
        print("Distiction")
    elif No >= 60:
        print("First class")
    elif No >=50:
        print("Second class")
    else:
        print("Fail")

def main():
    No = int(input("Enter a number: "))
    grade(No)

if __name__=="__main__":
    main()