#1. checking if the file exsists in the same directory
#def practice():
#    fname = input("Enter the name of the file: ")
#    try:
#        with open(fname,'r'):
#            print(f"FIle {fname} exists in the current directory")
#    except:
#        print(f"The file {fname} does not exists in the current directory")
#practice()

#2. Reading the contents of the file
#def practice():
#    fname = input("Enter file name: ")
#    try:
#        fobj = open(fname,'r')
#        content1 = fobj.read()
#        print(content1)
        # output is Jay Ganesh
        # Jay Jagdamb
        # Jay Shivray, entire file
#        content2 = fobj.readline()
#        print(content2)
        # output is Jay Ganesh, first line
#        content3 = fobj.readlines()
#        print(content3)
        # output is [Jay Ganesh\n, Jay Jagdamb\n, Jay Shivray] , all the content in list form
#    except:
#        print(f"File with name {fname} does not exists")   
#practice()

#3. copy content of one file to another
#def practice():
#    fname1 = input("Enter the file to copy the content from: ")
#    fname2 = input("Enter the file to copy the contents to: ")
#    try:
#        fobj1 = open(fname1,'r')
#        fobj2 = open(fname2,'w')
#        fobj2.write(fobj1.read())
#        print("Copied file")
#    except:
#        print("File copy falied")
#practice()

#4 check if both file have same content
#import sys
#def practice():
#    if len(sys.argv) != 3:
#        print("The command should look like: programfilename.py FirstFile SecondFile")
#        return   
#    fname1 = sys.argv[1]
#    fname2 = sys.argv[2]
#    try:
#        with open(fname1,'r') as f1:
#            with open(fname2,'r') as f2:
#                content = f1.read()
#                content1 = f2.read()
#                if content == content1:
#                    print("Both files have same content")
#                else:
#                    print("Both files doesnt contain the same content")
#    except:
#        print("Falied Comparison")
#practice()

# check if a particular word exists in the file

import sys
def practice():
    if len(sys.argv)!=3:
        print("Usage: ProgramFileName FileName WordToCompare")
        return
    fname = sys.argv[1]
    word = sys.argv[2]
    try:
        with open(fname,'r') as f:
            count = 0
            for line in f:
                if word in line:
                    count+=1
            print(count,word)
    except:
        print("No word")   
practice()