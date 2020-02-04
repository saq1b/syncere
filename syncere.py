# Primary file
import os
from colorama import init
from termcolor import colored
import subprocess
import sys
init()
devPath="/mnt/m_external_sd/Cooee/.m/"
localPath='./'
justList=False
if (len(sys.argv)>1):
    for i in sys.argv:
        if i=='-l':
            sys.argv.remove(i)
            justList=True
if len(sys.argv)>=3 and sys.argv[2]!='':
    localPath=sys.argv[2]
    if localPath[len(localPath)-1]!='/':   # if the user forgets to put / at last
        localPath+='/'
# print(localPath)
if sys.argv[1]!='':
    devPath=sys.argv[1]
    if devPath[len(devPath)-1]!='/':   # if the user forgets to put / at last
        devPath+='/'
# print(devPath)
print("Will copy files from " + devPath)
files=os.listdir(localPath)
# os.system()
# files=subprocess.check_output("dir "+localPath+" /b *.mp3", shell=True).decode().split('\r\n')
for i in files:
    if not i.endswith('mp3'):
        files.remove(i)
files=set(files)
cmd="adb shell ls -a " + devPath # +"*.mp3"
deviceFiles=subprocess.check_output(cmd,shell=True).decode().split('\r\r\n')
for i in deviceFiles:  # repetative code
    if not i.endswith('mp3'):
        deviceFiles.remove(i)
deviceFiles=set(deviceFiles)
filesToSend=files-deviceFiles-{''}
filesToReceive=deviceFiles-files-{''}
def printList(a):
    c=1
    for i in a:
        print(c,i)
        c+=1
# print(colored("On PC", "blue"))
# print(files)
# print(colored("On device", "red"))
# print(deviceFiles)
print(colored("Files To Receive", "green", "on_white"))
printList(filesToReceive)
print(colored("Files To Send", "red","on_white"))
printList(filesToSend)
choice=int(input("1. Pull From Device\n2. Push to device "))
def _pull():
    # size=0
    count=0
    for f in filesToReceive:
        count+=1
        # size+=os.path.getsize(f)
        if(not justList):
            cmd="adb pull \""+devPath+str(f)+"\" \""+localPath+str(f)+"\""
            os.system(cmd)
        print(colored(str(count) + ' ' + str(f)), "green")
    # print(str(size/1000000) + " Mb")
def _push():
    size=0
    count=0
    for f in filesToSend:
        count+=1
        size+=os.path.getsize(localPath+f)
        if(not justList):
            cmd="adb push \""+localPath+str(f)+"\" \""+devPath+str(f)+"\""
            os.system(cmd)
        print(colored(str(count) + ' ' + str(f), "green"))
    if(not justList):
        os.system("adb shell rm "+str(devPath)+"/"+sys.argv[0])
    print(str(size/1000000) + " Mb")
if choice==1:
    _pull()
if choice==2:
    _push()