# command line input 
import os
import psutil
import sys
import schedule
import time
import threading
import smtplib
from email.message import EmailMessage


def send_mail(sender, app_password, receiver, subject, body, attachment_path):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    # ✅ Add attachment
    with open(attachment_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(attachment_path)

        msg.add_attachment(file_data,
                            maintype="text",
                            subtype="plain",
                            filename=file_name)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

    print("Mail sent with attachment successfully")


def CreateLog(FolderName):

    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
    else:
        os.mkdir(FolderName)
        print("Directory for log file gets created sucsessfullt")

    #if not os.path.exists(FolderName):
       # os.mkdir(FolderName)
       
    Timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    Filename = os.path.join(FolderName,"1Marvellous_%s.log" %Timestamp)
    print("Log file gets created with: ", Filename)

    fobj = open(Filename,"w")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Survellance System------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-----------System Report--------------------------\n")
    #print("CPU usage: ",psutil.cpu_percent())
    fobj.write("CPU usage: %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    #print("RAM usage: ",mem.percent)
    fobj.write("RAM usage: %s %%\n" %mem.percent)
    fobj.write(Border+"\n")


    fobj.write("\n Disk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")


    # how much data sent and recevied
    net = psutil.net_io_counters()
    fobj.write("\nNetwork usage report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
    fobj.write("recv : %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process log
    Data = ProcessScan()
    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border+"\n")
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n " %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write("Number. od threads : %s\n" %info.get("num_threads"))
        num_file_name = len(info.get("open_files",[]))
        fobj.write("Open number of files: %s\n"  %num_file_name)
        fobj.write("Rss (Resident set size) in MB : %.2f\n" %info.get("rss_mb"))
        fobj.write("Virtual Memory (MB) : %.2f\n" %info.get("virtual_memory"))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------End of log file----------------\n")
    fobj.write(Border+"\n")

    log_file = Filename

    sender_email = "mailtestingapplication123456@gmail.com"
    app_password = "zkth iqui nxce ysfj"
    receiver_email = "mailtestingapplication123456@gmail.com"

    subject = "Marvellous System Surveillance Report"
    body = "Attached is the latest system log file."
    fobj.close()
    send_mail(sender_email, app_password, receiver_email, subject, body, log_file)

    return Filename


def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)

    # similar to os.walk
    # process_iter is like ps aur
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # convert create time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["num_threads"] = proc.num_threads()
            
            try:
                mem = proc.memory_info()
                info["rss_mb"] = mem.rss / (1024 * 1024)
                info["virtual_memory"] = mem.vms / (1024 * 1024)
            except:
                info["rss_mb"] = 0
                info["virtual_memory"] = 0

            try:
                info["open_files"] = proc.open_files()
            except psutil.AccessDenied:
                info["open_files"] = []

            listprocess.append(info)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    listprocess = sorted(listprocess, key=lambda x: x.get("rss_mb", 0), reverse=True)

    return listprocess[:10]

def main():

    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Survellance System------")
    
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to: ")
            print("1. Create automatic logs")
            print("2: Executes periodically")
            print("3: Sends mail with the log")
            print("4: Stores information about processess")
            print("5: Stores information about CPU")
            print("4: Stores information about RAM usage")
            print("4: Stores information about Secondary storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval: The time in minutes for periodic scheduling")
            print("DirectoryName: Name of directory to created auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous

    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval: ", sys.argv[1])
        print("Directory Name: ", sys.argv[2])

        #Apply the schedualar
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Survellance System started sucessfully")
        print("Directory created with name: ",sys.argv[2])
        print("TImeinterval in minutes: ",sys.argv[1])

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)
    
if __name__ == "__main__":
    main()