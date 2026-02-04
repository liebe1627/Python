import hashlib
import os

def checksum(filename):
    
    fobj = open(filename,'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
    if (len(Buffer)<0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def main():
    filename = os.path.abspath(input("Enter file name to calculate checksum: "))
    checksum(filename)
    print("Checksum of file is :",checksum(filename))

if __name__ == "__main__":
    main()