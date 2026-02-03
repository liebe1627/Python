import threading

ListX = [1,2,3,4,5,6,7]
def prime():
    primeList = []
    
    for i in ListX:
        if i <= 1:
            continue
        count = 0
        for j in range(1,i+1):
            if i % j==0:
                count+=1
        if count == 2:
            primeList.append(i)
    print("Prime numbers:", primeList)

def Notprime():
    NotPrimelist = []
    
    for i in ListX:
        if i <= 1:
            NotPrimelist.append(i)
            continue
        count = 0
        for j in range(1,i+1):
            if i % j==0:
                count+=1
        if count != 2:
            NotPrimelist.append(i)
    print("Not prime numbers:", NotPrimelist)

def main():
    t1 = threading.Thread(target=prime)
    t2 = threading.Thread(target=Notprime)
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()