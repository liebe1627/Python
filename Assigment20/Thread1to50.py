import threading
import time 
def ascending():
    for i in range(1,51):
        print("Ascending is ",i)

def descending():
    for i in range(50,0,-1):
        print("Descending is ",i)

def main():
    start_time = time.time()
    t1 = threading.Thread(target=ascending)
    t2 = threading.Thread(target=descending)

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    end_time = time.time()
    print("Time taken:", end_time - start_time)
 
if __name__=="__main__":
    main()