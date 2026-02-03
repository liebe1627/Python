from functools import reduce

size = int(input("Enter the size of list: "))
ListOfnumber = list()
print("Enter the list of numbers")

for i in range(size):
    value = int(input("Enter the number: "))
    ListOfnumber.append(value)
    

greaterThan70 = lambda i : i>= 70
AddTen = lambda i : i+10
Product = lambda a,b : a*b

Greater = list(filter(greaterThan70,ListOfnumber))
print(Greater)

Adding = list(map(AddTen,Greater))
print(Adding)

Product = reduce(Product,Adding)
print(Product)
