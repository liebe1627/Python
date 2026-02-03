from functools import reduce

Product = lambda a,b : a*b

def main():
    ListP = [1,2,3,4,5]
    Pro = reduce(Product,ListP)
    print("Product is: ",Pro)

if __name__=="__main__":
    main()