import io
def Checkingfile():
    fname = input("Enter the name of the file : ")

    try:
        with open(fname,'r'):
            print(f"{fname} exists in the current directory")
    except FileNotFoundError:
        print(f"{fname} does not exists in the current directory")

Checkingfile()
        


