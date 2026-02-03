def countstring():
    fname = input("Enter the file name: ")
    search = input("Enter the word to search: ")
    found = False
    try:
        with open(fname,'r') as f:
            for line in f:
                if search in line:
                    found = True
        if found:
            print(f"The {search} word exists in the file")
        else:
            print(f"The {search} word does not exists in the file")


    except FileNotFoundError:
        print("File does not exists")

countstring()