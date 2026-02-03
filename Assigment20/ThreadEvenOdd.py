import threading
import time

def Even():
    for i in range(2,21,2):
        print("Even number: ",i)

def Odd():
    for i in range(1,22,2):
        print("Odd number: ",i)

def main():
    Start_Time = time.time()
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    End_Time = time.time()
    print("Time taken:", End_Time - Start_Time)

if __name__=="__main__":
    main()
    