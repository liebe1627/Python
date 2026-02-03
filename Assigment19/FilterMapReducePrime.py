from functools import reduce

size = int(input("Enter the size of list: "))
ListOfnumber = list()
print("Enter the list of numbers")

for i in range(size):
    value = int(input("Enter the number: "))
    ListOfnumber.append(value)

def prime(a):

    if a <=1:
        print("Not prime")
        
    for i in range(2,a):
        if a%i==0:
            return False
    return True
            
    

MultiByTwo = lambda a : a*2
MaxBetweenTwo = lambda a,b: b if b>a else a

PrimeNumber = list(filter(prime,ListOfnumber))
print(PrimeNumber)

Multi = list(map(MultiByTwo,PrimeNumber))
print(Multi)

Maximum = reduce(MaxBetweenTwo,Multi)
print(Maximum)