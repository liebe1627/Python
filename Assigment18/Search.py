def main():
    print("Enter the number of elemets: ")
    size = int(input())
    
    Data = list()
    print("Enter the elements:")

    for i in range(size):
        value = int(input())
        Data.append(value)
    
    SearchNo = int(input("Enter a value to search in the list: "))

    count = 0
    for i in range(size):
        if SearchNo == Data[i]:
            count+=1
    print(count)

if __name__=="__main__":
    main()
