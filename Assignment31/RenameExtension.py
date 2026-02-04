import os
import sys
def DisplayFileExtension(Directory, Extension1, Extension2):

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
            if(fname.endswith(Extension1)):
                print(fname.replace(Extension1, Extension2 ))
            
def main():
    if len(sys.argv)!=4:
        print("Usage: python3 DisplayFileExtensionDir.py /User/Python .txt")
        return
    
    FolderName = os.path.abspath(sys.argv[1])
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]
    if not Extension1.startswith('.'):
        Extension1 = '.' + Extension1
    
    if not Extension2.startswith('.'):
        Extension2 = '.' + Extension2

    DisplayFileExtension(FolderName, Extension1, Extension2)

if __name__ == "__main__":
    main()