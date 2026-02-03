import functools

Even = lambda a: a%2==1

def main():
    ListE = [1,2,3,4,5,6,7,9]
    EvenFilter = list(filter(Even,ListE))
    print("List of even is: ",EvenFilter)

if __name__=="__main__":
    main()