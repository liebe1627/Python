#Greatest between two number
def GreaterBetweenTwo(No1,No2):
    if No1>No2:
        print("No1 is greater than No2 with value of No1 being:",No1)
    else:
        print("No2 is greater than No1 with value if No2 being:",No2)
def main():
    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter secnond number:"))
        
    GreaterBetweenTwo(No1,No2)
    
if __name__=="__main__":
    main()
