from functools import reduce

Add = lambda a,b:a+b

def main():
    Data =[1,2,3,4,5]
    ReduceData = reduce(Add,Data)
    print("Redunced data is: ",ReduceData)

if __name__=="__main__":
    main()

