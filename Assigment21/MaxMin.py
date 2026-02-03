import threading
Listx = [1,2,3,4,5,6]
def Maximum():
    maxvalue = Listx[0]
    for i in Listx:
        if i > maxvalue:
            maxvalue = i
    print(maxvalue)

def Minimum():
    minvalue = Listx[0]
    for i in Listx:
        if i < minvalue:
            minvalue = i
    print(minvalue)

def main():
    t1=threading.Thread(target=Maximum)
    t2=threading.Thread(target=Minimum)
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__=="__main__":
    main()