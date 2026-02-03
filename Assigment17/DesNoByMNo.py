def Stars(No):
    for i in range(No+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        

def main():
    No = int(input("Enter a number: "))
    Stars(No)

if __name__=="__main__":
    main()