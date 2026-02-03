def ListPrime():
    size = int(input("Enter the size of list: "))
    ListOfNumber = list()
    print("Enter the values in the list: ")

    for i in range(size):
        Value = int(input())
        ListOfNumber.append(Value)
    return ListOfNumber
