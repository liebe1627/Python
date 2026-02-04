import hashlib
import os

def FindDuplicate(Dictionary):
    ret = False

    ret = os.path.exists(Dictionary)
    if ret == False:
        print("Directory does not exists")
        return
    
    ret = os.path.isdir(Dictionary)
    if ret == False:
        print("Invalid Directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(Dictionary):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            checksum = Checksum(fname)
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
    return Duplicate

def DeleteDupli(Dictionary):
    mydict = FindDuplicate(Dictionary)
    if not mydict:
        return []
    result = list(filter(lambda x:len(x)>1,mydict.values()))
    listOfDupli = []
    for values in result:
        count = 0
        for value in values:
            count+=1
            if count>1:
                listOfDupli.append(value)
    Duplicates = listOfDupli    

    logfolderBase = "/Users/omkarnagnure/Vaishnavi/PythonPrograms/Python"
    logfolder = os.path.join(logfolderBase,"Logs")

    if not os.path.exists(logfolder):
        os.makedirs(logfolder,exist_ok=True)

    logfile = os.path.join(logfolder,"DeleteFilesLog.Log")

    logobj = open(logfile,'w')

    Border = "-"*80
    logobj.write(Border+"\n")

    logobj.write("Directory Automation: List of Deleted files which are duplicate\n")

    logobj.write(Border+"\n")

    for files in Duplicates:
        logobj.write(files+"\n")
        os.remove(files)
    logobj.write(Border+"\n")
                      

def Checksum(filename):
    
    fobj = open(filename,'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():
    Dictionary = input("Enter Directory name: ")
    DeleteDupli(Dictionary)
    
if __name__ == "__main__":
    main()