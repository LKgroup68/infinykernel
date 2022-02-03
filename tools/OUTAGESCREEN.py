import os
import time
os.system("clear")
print("-=INFINY KERNEL OUTAGESCREEN=-")
print("YOUR SYSTEM/COMPUTER HAVE A PROBLEM")
print("RESTARTING IN 3SEC")
time.sleep(3)
os.system("clear")
print("INFINY KERNEL")
print("MINIMUM SHELL")
while(1):
  cmd = input("DEBUG\>")
  if cmd == "help":
    print("DEBUGGING HELP\nhelp : DOWNLOAD LKOS IN INTERNET SERVER AND REBOOT IN/ not requires internet connexion\nreboot : REBOOT THE SYSTEM\nstart : RESTART IN INFINY KERNEL NORMAL")
  if cmd == "reboot":
    os.system("python3 OUTAGESCREEN.py")
  if cmd == "start":
    os.system("python3 main.py")
  
