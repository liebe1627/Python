def Divible(No):
    if No%5==0:
        print("Divisibel by 5")
    else:
        print("Not divisible by 5")
    
def main():
    No = int(input("Enter a number: "))
    Divible(No)

if __name__=="__main__":
    main()