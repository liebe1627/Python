import io
def Checkingfile():
    fname = input("Enter the name of the file : ")

    try:
        with open(fname,'r') as f:
            print(f"{fname} exists in the current directory")
            content = f.read()
            print("File content: ",content)

    except FileNotFoundError:
        print(f"{fname} does not exists in the current directory")

Checkingfile()
        


