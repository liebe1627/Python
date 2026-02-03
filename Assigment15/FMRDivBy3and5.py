import functools

Divisible = lambda a: a%3==0 and a%5==0

def main():
    ListD = [1,2,3,4,5,6,7,8,9,10,15]
    Div = list(filter(Divisible,ListD))
    print("Divisible by 3 and 5: ",Div)

if __name__=="__main__":
    main()