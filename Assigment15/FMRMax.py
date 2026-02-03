from functools import reduce

Max = lambda a,b : a if a>b else b

def main():
    ListM = [1,2,3,4,5,6,7]
    Maxreduce = reduce(Max,ListM)
    print("Max from list is: ",Maxreduce)

if __name__=="__main__":
    main()