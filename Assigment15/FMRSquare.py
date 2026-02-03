import functools 

Square = lambda a : a**2

def main():
    listM = [1,2,3,4,5,6]
    Mapping = list(map(Square,listM))
    print("Data after mapping: ",Mapping)
    
if __name__ == "__main__":
    main()