import threading

listX = [1,2,3,4,5]
def sumofno():
    total = 0
    for i in listX:
        total+=i
    print(total)

def product():
    total = 1
    for i in listX:
        total=total*i
    print(total)

def main():
    t1 = threading.Thread(target=sumofno)
    t2 = threading.Thread(target=product)
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__=="__main__":
    main()