import os
import subprocess
import sys
files=os.listdir('.')
files=set(files)
devPath="/mnt/m_external_sd/Cooee/.m/"
cmd="adb shell ls -a " + devPath 
deviceFiles=subprocess.check_output(cmd,shell=True).decode().split('\r\r\n')
deviceFiles=set(deviceFiles)
filesToCopy=files-deviceFiles
size=0
count=0
justList=False
if (len(sys.argv)>1 and sys.argv[1]=='-l'):
    justList=True
for f in filesToCopy:
    count+=1
    size+=os.path.getsize(f)
    if(not justList):
        cmd="adb push "+str(f)+" "+devPath+str(f)
        os.system(cmd)
    print(str(count) + ' ' + str(f))
if(not justList):
    os.system("adb shell rm "+str(devPath)+"/"+sys.argv[0])
print(str(size/1000000) + " Mb")
