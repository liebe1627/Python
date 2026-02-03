def CountLines():
    fname = input("Enter file name: ")
    count = 0
    try:
        with open(fname,'r') as f:
            for line in f:
                count+=1
        print(f"The number of lines in the file are {count}")
    
    except FileNotFoundError:
        print("The file does not exists")
CountLines()