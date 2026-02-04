import os
import sys
import shutil

def CopyDirectory(Directory1, Directory2):
    ret1 = False

    ret1 = os.path.exists(Directory1)
    if ret1 == False:
        print("Source Directory does not exists")
        return
    
    ret1 = os.path.isdir(Directory1)
    if ret1 == False:
        print("Source Directory Does not exists/Invalid Directory")
        return
    
    for FolderName1, SubFolderName1, FileName1 in os.walk(Directory1):
        for fname in FileName1:
            relative_path = os.path.relpath(FolderName1, Directory1)
            Dest_Folder = os.path.join(Directory2, relative_path)

            os.makedirs(Dest_Folder,exist_ok=True)

            for fname in FileName1:
                srcfiles = os.path.join(FolderName1,fname)
                desflies = os.path.join(Dest_Folder,fname)
                shutil.copy2(srcfiles,desflies)
                print(f"Copied file are {desflies}")    
def main():
    if len(sys.argv)!=3:
        print("usageL python3 CopyDirectory.py <Source Directory> <Destination Directory>")
        return
    
    Directory1 = os.path.abspath(sys.argv[1])
    Directory2 = os.path.abspath(sys.argv[2])

    CopyDirectory(Directory1, Directory2)


if __name__ == "__main__":
    main()