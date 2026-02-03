def main():
    print("Enter the number of elemets: ")
    size = int(input())
    
    Data = list()
    print("Enter the elements:")

    for i in range(size):
        value = int(input())
        Data.append(value)
    
    print("Max is: ",min(Data))

if __name__=="__main__":
    main()
