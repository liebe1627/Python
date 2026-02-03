def main():
    print("Enter the number of elemets: ")
    size = int(input())
    
    Data = list()
    print("Enter the elements:")

    for i in range(size):
        value = int(input())
        Data.append(value)
    
    sum = 0
    for i in range(size):
        sum+=Data[i]
    print("summation is: ",sum)

if __name__=="__main__":
    main()
