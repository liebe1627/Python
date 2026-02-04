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
    return listOfDupli                
            
            

def Checksum(filename):
    
    fobj = open(filename,'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
    while Buffer:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def main():
    Dictionary = input("Enter Directory name: ")
    Duplicates = DeleteDupli(Dictionary)
    logfilepath = "/Users/omkarnagnure/Vaishnavi/PythonPrograms/Python"
    logfile = os.path.join(logfilepath,"DuplicateFilesLog.Log")
    logobj = open(logfile,'w')
    Border = "-"*80
    logobj.write(Border+"\n")
    logobj.write("Directory Automation: List of Duplicate files\n")
    logobj.write(Border+"\n")
    for files in Duplicates:
        logobj.write(files+"\n")
    logobj.write(Border+"\n")
    
if __name__ == "__main__":
    main()