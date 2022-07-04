from cgitb import text
from dataclasses import replace
from datetime import datetime
from turtle import pensize   
f=open( "D:\\Documents\\Codes\\DataScienceBootcamp\\Session3\\x.txt",'r')
lines=f.readlines()
print(lines)
print("--------------------------------------------------")
print((lines[1::2]))
ll=lines[1::2]
print((ll)[-1])
print("--------------------------------------------------")
txt=(" ".join(ll).lower())
txt.lower()
print("/-*/-*/*-/-/-/*-/*-/-*/*-//-",txt)
print(len(txt.split("\n")))
unwanted='?!.,'
for x in unwanted:
    if x in txt:
        txt=txt.replace(x," ")
txt=txt.replace("\n"," ")
print(txt)
w=[]
freq={}
for x in txt.split():
    if x not in freq:
        freq[x]=1
    else :
        freq[x]+=1
print(sorted(freq.items(),key=lambda x:x[-1])[-5:])