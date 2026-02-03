def NaturalNumber(No1):
    Sum = 0
    for i in range(1,No1+1):
        Sum += i
    print(f"Sum of all natural numbers for {No1} is:", Sum)

def main():
    No1=int(input("Enter a number: "))
    NaturalNumber(No1)

if __name__=="__main__":
    main()