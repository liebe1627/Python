def prime(No):
    count = 0
    if No<=1:
        print("Not a prime number ",No)
    else:
        for i in range(1,No+1):
            if No%i==0:
                count+=1
        if count==2:
            print("Prime number")
        else:
            print("Not a prime number")
def main():
    No = int(input("Enter a number: "))
    prime(No)

if __name__=="__main__":
    main()