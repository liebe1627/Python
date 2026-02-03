def Digits(No):
    count = 0
    while No > 0:
        count +=1
        No=No//10
    return count

def main():
    No = int(input("Enter a number: "))
    D = Digits(No)
    print(D)

if __name__=="__main__":
    main()