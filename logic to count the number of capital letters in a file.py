#Write Python logic to count the number of capital letters and Lower case letters in a file

import os
#os.chdir('C:\\Users\\lifei\\Desktop')
with open("C:\\Users\\CHANDAN\\Desktop\\Python_StudyMaterial.txt") as today:
    count1=0
    count2=0
    for i in today.read():
        if(i.islower()):
            count1=count1+1
        elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
