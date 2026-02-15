import os
import sys
import schedule
import time
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def UnzipFile(zip_file, destination):
    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_file, "r") as zobj:
        zobj.extractall(destination)

    return destination

def send_mail(sender, receiver, subject, body, app_password , file_path , zip_file):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(file_path, "rb") as file:

        file_data = file.read()
        file_name = os.path.basename(file_path)

        msg.add_attachment(file_data,
                            maintype="text",
                            subtype="plain",
                            filename=file_name)
        
    with open(zip_file, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(zip_file)

        msg.add_attachment(file_data,
                            maintype="application",
                            subtype="zip",
                            filename=file_name)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

def make_zip(foldername):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = foldername + "_" + timestamp + ".zip"
    zobj = zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(foldername):
        for file in files:
            if not file.endswith((".zip",'.tmp','.log')):
                full_path = os.path.join(root,file) 
                relative = os.path.relpath(full_path,foldername)
                zobj.write(full_path,relative)
    zobj.close()

    return zip_name
    
def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path,"rb")
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()

def BackupFiles(Source,Destination):

    copied_files = []

    print("Creating teh backup folder for backup process")

    os.makedirs(Destination , exist_ok=True) 

    for root, dirs, files in os.walk(Source):

        for file in files:

            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)

            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or calculate_hash(src_path) != calculate_hash(dest_path):
                shutil.copy2(src_path,dest_path) 
                copied_files.append(relative)

    return copied_files


def MarvellousDataShieldStart(Source="Data"):

    folder_name = "Logs"

    Ret = False

    Ret = os.path.exists(folder_name)

    if Ret == True:
        Ret = os.path.isdir(folder_name)
        if Ret == False:
            print("Unable to create folder")
    else:
        os.makedirs(folder_name,exist_ok=True)
        print("Directory for log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    file_path = os.path.join(folder_name, "MarvellousDataShield%s.log" %timestamp)
    print("Log file created with name:",file_path)

    fobj = open(file_path,"w")
    Border = "-"*50
    BackupName = "MarvellousBackup"

    fobj.write(Border+"\n")

    fobj.write("Backup process started successfully at:" + time.ctime() + "\n")

    fobj.write(Border)

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)
    
    for file in files:
        fobj.write(file + "\n")

    fobj.write(Border)

    fobj.write("Backup completed sucessfully"+ "\n")
    fobj.write("Files copied : " + str(len(files)) + "\n")
    fobj.write("Zip file gets created: " + zip_file + "\n")

    fobj.write(Border)

    sender = "mailtestingapplication123456@gmail.com"
    app_password = "zkth iqui nxce ysfj"
    receiver = "mailtestingapplication123456@gmail.com"
    subject = "Marvellous Data Shield BAckup Report"
    body = f"""
    Hello,
    Please find attached:
    1. Backup Log File
    2. Backup Zip Archive
    Backup Time: {time.ctime()}
    Regards,
    Marvellous Data Shield
    """

    fobj.close()
    sendmail = send_mail(sender, receiver, subject, body, app_password , file_path , zip_file)
    print("Marvellous Mail Sent Successfully")

def main():

    Border = "-"*50
    print(Border)
    print("--------Marvellous Data Shield System--------")
    
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to: ")
            print("1. Takes auto - backup at given time")
            print("2. Backup only new and updated files")
            print("3. Create an archive of the backup periodically")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic scheduling")
            print("DirectoryName: Name of directory to created auto logs")
            print("Source directory: Name of directory to be backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")


    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval: ", sys.argv[1])
        print("Directory Name: ", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data shield System started sucessfully")
        print("TImeinterval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the executiom")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv)==4):
        if sys.argv[1] == "--restore":
            print("Restoring the backup from the zip file")

            zip_file = sys.argv[2]
            destination = sys.argv[3]

            Extract_zip = UnzipFile(zip_file, destination)

            print("Backup restored successfully to:", Extract_zip)
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)
    
if __name__ == "__main__":
    main()