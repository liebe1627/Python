import sys
def compare():
    if len(sys.argv) != 3:
        print("Usage: python compare.py file1 file2")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        with open(file1,'r') as f1, open(file2,'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                print("Sucess")
            else:
                print("Failure")
    except FileExistsError:
        print("One or both files do not exist")
compare()
