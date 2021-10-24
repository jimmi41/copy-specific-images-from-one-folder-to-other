import csv
import shutil
import os
import fnmatch
from typing import List, Pattern

listOfImageId=[]
listOfSentiment=[]
mapRnAndImgid={}
removed=0
with open('insta1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rownumber = 0
    for row in csv_reader:
        if row[1]==row[2] and row[2]==row[3]:
            rownumber=rownumber+1
            removed=removed+1
            listOfSentiment.append("null")
            continue
        elif row[1]>max(row[2],row[3]):
            listOfSentiment.append("positive")
        elif row[2]>row[3]:
            listOfSentiment.append("neutral")
        else:
            listOfSentiment.append("negative")
        
        str=row[0]+".jpg"
        
        mapRnAndImgid[str]=rownumber
        listOfImageId.append(str)
        rownumber=rownumber+1
  
        
cp=0
cn=0
cneu=0
n=0
for it in listOfSentiment:
    if it=="null":
        n=n+1
    elif it == "positive":
        cp=cp+1
    elif it == 'neutral':
        cneu=cneu+1
    else:
        cn=cn+1
        


src= r'C:\Users\anupa\Desktop\src\csv\instaPhotos'

destNeutral=r'C:\Users\anupa\Desktop\src\csv\instaNeutral'

destNegative=r'C:\Users\anupa\Desktop\src\csv\instaNeg'

destPositive=r'C:\Users\anupa\Desktop\src\csv\instaPos'

c=0
os.chdir(src)
for f in os.listdir():
    if f in listOfImageId:
        
        rn=mapRnAndImgid[f]
        if listOfSentiment[rn]=="null":
            continue
        elif listOfSentiment[rn] == "positive":
            
            dest=destPositive
        elif listOfSentiment[rn] == "negative":
            
            dest=destNegative
        else:
            
            dest=destNeutral
        print(c)
        c=c+1
        shutil.copy(f,dest)
print(" total positive are ",cp)
print(" total negative are ",cn)
print(" total neutral are :",cneu)
print(" total cp+cn+cnew are :",(cneu+cp+cn))
print(" total null data",n)
print(" total removed due to equal point in pos neg and neutral: ",removed)



