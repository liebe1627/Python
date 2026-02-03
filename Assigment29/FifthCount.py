def countstring():
    fname = input("Enter the file name: ")
    search = input("Enter the word to search: ")

    count = 0
    try:
        with open(fname,'r') as f:
            for line in f:
                count += line.count(search)
        print(f"Count of the word {search} in file is {count}")

    except FileExistsError:
        print("File does not exists")

countstring()