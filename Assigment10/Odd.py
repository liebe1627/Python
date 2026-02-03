def Odd(No1):
    for i in range(No1+1):
        if i%2==1:
            print(i)

def main():
    No1 = int(input("Enter a number: "))
    Odd(No1)

if __name__=="__main__":
    main()