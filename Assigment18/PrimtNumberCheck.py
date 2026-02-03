import PrimeAddition

ListX = PrimeAddition.ListPrime()
print(ListX)
count = 0
def CheckPrime():
        for i in ListX:

            if i<=1:
                print("Not prime")

            for j in range(2,i):
                 if i%j==0:
                      count+=1
            
        if count==2:
            print("Not a prime")
        else:
            print("Prime")

CheckPrime()


