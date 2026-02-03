def Checkingfile():
    fname = input("Enter the name of the file source file : ")
    f2name = input("Enter the name of the file destination file : ")

    try:
        with open(fname,'r') as f1:
            with open(f2name,'w') as f2:
                f2.write(f1.read())
                
        print("File sucessfully copied")

    except FileNotFoundError:
        print(f"{fname} does not exists in the current directory")

Checkingfile()
        


