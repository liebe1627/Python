from functools import reduce

Min = lambda a,b : a if a<b else b

def main():
    ListM = [1,2,3,4,5,6,7]
    Minreduce = reduce(Min,ListM)
    print("Max from list is: ",Minreduce)

if __name__=="__main__":
    main()