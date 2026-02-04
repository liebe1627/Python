import os
import sys
def DisplayFileExtension(Directory, Extension):

    ret = False

    ret = os.path.exists(Directory)
    if (ret == False):
        print("Given path does not exists")
        return
    
    ret = os.path.isdir(Directory)
    if (ret == False):
        print(f"Directory named {Directory} does not exists")
        return

    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            if(fname.endswith(Extension)):
                print(fname)
            

def main():
    if len(sys.argv)!=3:
        print("Usage: python3 DisplayFileExtensionDir.py /User/Python .txt")
        return
    
    FolderName = os.path.abspath(sys.argv[1])
    Extension = sys.argv[2]
    if not Extension.startswith('.'):
        Extension = '.' + Extension

    DisplayFileExtension(FolderName, Extension)

if __name__ == "__main__":
    main()