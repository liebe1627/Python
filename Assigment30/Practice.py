#Count lines in a file
# def practice(fname):
#     try:
#         with open(fname,"r") as f:
#             count = 0
#             for line in f:
#                 count +=1
#         print("The number of files is:", count)
#     except FileNotFoundError:
#         print("Was not able to find the file")

#count words
# def practice(fname):
#     try:
#         with open(fname,'r') as f:
#             count = 0
#             for lines in f: # a line
#                 #for line in lines: # each letter
#                 word = lines.split()
#                 Lengthofword = len(word)
#                 count+=Lengthofword
#         print(count)
#     except FileExistsError:
#         print("File does not exists")

#To display each line by line
# def practice(fname):
#     try:
#         with open(fname,'r') as f:
#             for line in f:
#                 print(line,end=" ")
#     except FileNotFoundError:
#         print("File not found")

#copy file contents into another file
# import shutil
# def practice(fname):
#     fname2 = "Demo.py"
#     try:
#         with open(fname,"r") as f:
#             with open(fname2,"r") as f1:
#                 shutil.copy2(fname,fname2)
#                 print(f"Copied code from {fname} to {fname2}")
#     except FileNotFoundError:
#         print("File not found")

#search word in a file
def practice(fname):
    search = "Jay"
    found = False
    try:
        with open(fname,"r") as f:
            for line in f:
                if search in line:
                    found = True

        if found:
            print(f"The {search} word exists in the file")
        else:
            print(f"The {search} word does not exists")

    except FileExistsError:
        print("File not found")
       
def main():
    fname = input("Enter file name: ")
    practice(fname)

if __name__ == "__main__":
    main()