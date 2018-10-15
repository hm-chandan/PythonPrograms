import sys,os               //importing system
import time                 //importing time module

ctime=time.strftime("%H:%M")    //printing time in hours minutes
print(ctime)

while ctime!=sys.argv[1]:       //passing ssytem time as argv[1]
    ctime=time.strftime("%H:%M")
    
os.system('mpv'+sys.argv[2])    //passing alert time as argv[2]
