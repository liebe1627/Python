def Table(No1):
    for i in range(1,11):
        Sum = i*No1 
        print(Sum)
def main():
    No1 = int(input("Enter a number: "))
    Table(No1)

if __name__=="__main__":
    main()
    