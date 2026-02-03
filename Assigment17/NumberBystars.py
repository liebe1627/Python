def Stars(No):
    for i in range(No):
        print("*"*No)

def main():
    No = int(input("Enter a number: "))
    Stars(No)

if __name__=="__main__":
    main()