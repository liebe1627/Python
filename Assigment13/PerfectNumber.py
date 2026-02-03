def perfect(No):
    sum = 0
    originalNumber = No
    if No == 0 or No<0:
        print("Number is not a perfect number")
        return
    
    for i in range(1,No):
        if No%i==0:
            sum=sum+i
    if sum == originalNumber:
        print("Perfact number")
    else:
        print("Not a perfect number")
    
def main():
    No = int(input("Enter a number: "))
    perfect(No)

if __name__=="__main__":
    main()