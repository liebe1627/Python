import os
import sys
import shutil

def DisplayFileExtension(Directory1,Directory2, Extension):

    ret = False

    ret = os.path.exists(Directory1)
    if (ret == False):
        print("Given path does not exists")
        return
    
    ret = os.path.isdir(Directory1)
    if (ret == False):
        print(f"Directory named {Directory1} does not exists")
        return
            
    for FolderName1, SubFolderName1, FileName1 in os.walk(Directory1):
        
        relative_path = os.path.relpath(FolderName1, Directory1)
        Dest_Folder = os.path.join(Directory2, relative_path)

        os.makedirs(Dest_Folder,exist_ok=True)

        for fname in FileName1:
            if fname.endswith(Extension):
                srcfiles = os.path.join(FolderName1,fname)
                desflies = os.path.join(Dest_Folder,fname)
                shutil.copy2(srcfiles,desflies)
                print(f"Copied file are {desflies}") 

def main():
    if len(sys.argv)!=4:
        print("Usage: python3 DisplayFileExtensionDir.py /User/Folder1 /User/Folder2 .txt")
        return
    
    FolderName1 = os.path.abspath(sys.argv[1])
    FolderName2 = os.path.abspath(sys.argv[2])

    Extension = sys.argv[3]
    if not Extension.startswith('.'):
        Extension = '.' + Extension

    DisplayFileExtension(FolderName1,FolderName2,Extension)

if __name__ == "__main__":
    main()