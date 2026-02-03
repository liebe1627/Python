import functools

CheckLen = lambda a: len(a)>5

def main():
    ListS = ["qwert","ertyuio","asdf","ASdfgh"]
    FilterX = list(filter(CheckLen,ListS))
    print("Length more than 5: ",FilterX)

if __name__=="__main__":
    main()