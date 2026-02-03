def stars(No):
    for i in range(No):
        print("*")

def main():
    No = int(input("Enter a number: "))
    stars(No)

if __name__=="__main__":
    main()