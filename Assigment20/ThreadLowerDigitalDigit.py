import threading
import time

upper=[]
lower =[]
digit =[]

def UpperCase(String1):
    print("Thread Id: ",threading.get_ident())
    print("Thread name: ",threading.current_thread().name)
    for ch in String1:
        if ch.isupper():
            upper.append(ch)

def LowerCase(String1):
    print("Thread Id: ",threading.get_ident())
    print("Thread name: ",threading.current_thread().name)
    for ch in String1:
        if ch.islower():
            lower.append(ch)

def Digits(String1):
    print("Thread Id: ",threading.get_ident())
    print("Thread name: ",threading.current_thread().name)
    for ch in String1:
        if ch.isdigit():
            digit.append(ch)

def main():
    String1 = input("Enter a string: ")
    t1 = threading.Thread(target=UpperCase,args=(String1,))
    t2 = threading.Thread(target=LowerCase,args=(String1,))
    t3 = threading.Thread(target=Digits,args=(String1,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    t3.start()
    t3.join()

    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Digits:", digit)
    
if __name__ == "__main__":
    main()
