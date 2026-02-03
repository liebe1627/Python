def Divisible(No1):
    if No1%3==0 and No1%5==0:
        print("The number divisible by 3 and 5 is: ",No1)
    else:
        print(f"The given number {No1} is not divisible by 3 and 5")

def main():
    No1 = int(input("Enter a number: "))
    Divisible(No1)

if __name__=="__main__":
    main()