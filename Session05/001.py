# read data from the following links:
# https://raw.githubusercontent.com/homsit/files/main/invdata1.txt
# https://raw.githubusercontent.com/homsit/files/main/invdata2.txt
# verify if there is a duplicate in each file (is there any bacode number that was scanned more than one time)
# find shared barcodes in both files
import requests
import re
res1=requests.get("https://raw.githubusercontent.com/homsit/files/main/invdata1.txt")
res2=requests.get("https://raw.githubusercontent.com/homsit/files/main/invdata2.txt")
#sp1=str(res1)
#print((res1.text).split(","),)
print("\n ++++++++++++++++++++++++++++++++++++ \n")
list1=re.findall("\d+",res1.text) # no need to [ ] its already list
list2=re.findall("\d+",res2.text)
freq={}
#print(list1)
for p in list1:
    if p not in freq:
        freq[p]=1
    else :
        freq[p]+=1
#print(freq)
freqq=sorted(freq.items(), key=lambda t:t[1])
print(freqq,"\n++++++++++++++\n")
freq_final = [(x,y) for x,y in freqq if y>1]
print(freq_final)

shared=[x[0] for x in freqq if x[0] in list2]
print("Shared : ",len(shared))
shared2=set(list1)& set(list2) #----------------------
print(len(shared2))

print("duplicate in 2 \n",len((list2)))
print("duplicate in 2 \n",len(set(list2))) #---------