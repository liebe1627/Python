def SquareOfNumber(No1):
   Res = No1**3
   print(Res)

def main():
    Value = int(input("Enter a number: "))
    SquareOfNumber(Value)

if __name__=="__main__":
   main()