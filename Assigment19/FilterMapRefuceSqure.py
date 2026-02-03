from functools import reduce

size = int(input("Enter the size of list: "))
ListOfNumber = list()

for i in range(size):
    Value = int(input("Enter the values: "))
    ListOfNumber.append(Value)

Even = lambda a : a%2==0
Square = lambda a : a**2
Additon = lambda a,b : a+b

EvenNumber = list(filter(Even,ListOfNumber))
print(EvenNumber)

SquareOfNumbers = list(map(Square,EvenNumber))
print(SquareOfNumbers)

AdditionOfAll = reduce(Additon,SquareOfNumbers)
print(AdditionOfAll)