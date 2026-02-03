import threading
import time

ListX = [1,2,3,4,5,6,7,8,9]

def EvenList():
    total=0
    for i in ListX:
        if i%2==0:
            total+=i
    print("Sum of even: ",total)

def OddList():
    total=0
    for i in ListX:
        if i%2==1:
            total+=i
    print("Sum of odd: ",total)

def main():
    start_time = time.time()
    t1 = threading.Thread(target=EvenList)
    t2 = threading.Thread(target=OddList)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print("Time taken:", end_time - start_time)

if __name__ == "__main__":
    main()