import threading
import time

def EvenFactor(No):
    factor = []
    for i in range(1,No+1):
        if No%i==0 and i%2==0:
            factor.append(i)
    print(factor) 

def OddFactor(No):
    factor = []
    for i in range(1,No+1):
        if No%i==0 and i%2==1:
            factor.append(i)
    print(factor) 

def main():
    start_time = time.time()
    t1 = threading.Thread(target=EvenFactor,args=(10,))
    t2 = threading.Thread(target=OddFactor,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Exit from main")
    end_time = time.time()
    print("Time taken:", end_time - start_time)


if __name__=="__main__":
    main()

        

