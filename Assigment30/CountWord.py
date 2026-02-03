def CountWord():

    fname = input("Enter the name of the file: ")
    count = 0 

    try:
        with open(fname,'r') as f:
            for line in f:
                words = line.split()
                count += len(words)
        print(f"Total number of words in the file are {count}")

    except FileNotFoundError:
        print("file does not exists")
        
CountWord()