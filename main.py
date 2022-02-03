import time
import os
import psutil
import shutil
from tkinter import*
print ("-=INFINTY CHECKER 0.0.3=-")
print("")
print("CKECKING COMPUTER AND LOADING SYSTEM...")


def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)
usage = shutil.disk_usage("/")
free_space = formatSize(usage[2])

CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

pid = os.getpid()
py = psutil.Process(pid)
ramuse = py.memory_info()[0]/2.**30 

print("------[COMPUTER SPECIFICATION]-------")
print ("RAM : OK")
print ("CPU :",CPU_Pct,"%")
print ("HARDDRIVE :",free_space,"free")  # Delays for 5 seconds. You can also use a float value.
print("-------------------------------------")
systemboot = os.path.exists('main.py')
systempathuser = os.path.exists('usr')
systempathapp = os.path.exists('app')
if systemboot == 1:
  print("SYSTEM BOOT......OK")
  time.sleep(1)
else:
  os.system("python3 OUTAGESCREEN.py")
if systempathuser == 1:
  print("USER STORAGE......OK")
  time.sleep(1)
else:
  os.system("python3 OUTAGESCREEN.py")
if systempathapp == 1:
  print("APP DIRECTORY......OK")
  time.sleep(1)
else:
  os.system("python3 OUTAGESCREEN.py")
print("-------------------------------------")
time.sleep(2)
os.system("clear")
print("INFINY KERNEL")
print("--------------")
print("")
while(1):
  command = input("KERNEL>")
  if command == "cpu":
   print ("CPU :",CPU_Pct,"%")
  if command == "vim":
   os.system("vim")
  if command == "hardfree":
   print ("Drive1 :",free_space,"free")
  if command == "reboot":
   print ("rebooting...")
   os.system("clear")
   os.system("python3 main.py")
  if command == "cdmgr":
   while(1):
    os.system("clear")
    print("quel fichier ?")
    os.system("ls -a")
    filemg = input("file>")
    os.chdir(filemg)
    if command == "exit":
      os.system("clear")
      break;
    
  if command == "looker":
   print("----link to dir------")
   os.system("pwd && echo is the actual repertory")
   print("-------FILES---------")
   os.system("ls -a")
   
  if command == "lpack":
   os.system("clear")
   print("quel package ?")
   while(1):
    lpack = input("package>")
    os.system("install-pkg " + lpack)
    os.system("clear")
    print("package installed")
    if command == "exit":
      break; 
  
  if command == "run":
   os.system("clear")
   print("what program to run")
   while(1):
    bash = input("run>")
    os.system("bash " + bash)
    os.system("clear")
    print("propgram stoped")
    if command == "exit":
     break;



  if command == "echo":
   while(1):
    bashe = input("echo>")
    if bashe == "exit":
     break;
    else:
      print(bashe)
      
  if command == "about":
   os.system("clear")
   print("LKOS VERSION 0.0.1")
   print("-----cpu(s)-----")
   print ("CPU :",CPU_Pct,"%")
   print("-----disque(s)-----")
   print ("INFINYTOSH :",free_space,"free")
   print("numero du pack LKOS001")
    

  if command == "clear":
   os.system("clear")
  if command == "task":
   print("pour stop : ctrl+C")
   time.sleep(5)
   os.system("htop")
  if command == "myfile":
   os.system("pwd")
  if command == "help":
   print("help system V0.1\nclear clear the screen\nabout says about the system\nhardfree see the free space in the disk\nreboot reboot the system\nlooker for see the curent directory\ncdmgr changing the directory\nlpack for install program\nrun for run program")
  if command == "exit":
   print ("exiting session")
   break;

    
os.system("clear")
print("INFINY KERNEL")
print("shell stopped")
