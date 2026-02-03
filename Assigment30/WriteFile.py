def WriteFile():

    fname = input("Enter the file name: ")

    try:
        with open(fname,'r') as f:
            for line in f:
                print(line,end='')

    except FileNotFoundError:
        print("File does not exists")

WriteFile()