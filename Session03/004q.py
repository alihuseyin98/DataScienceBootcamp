# D:\\Personal\\Courses\\DCBootCamp\\dosyalar\\session3\\chat.txt
from datetime import datetime
#extract the names of speakers :
f=open( "D:\\Personal\\Courses\\DCBootCamp\\dosyalar\\session3\\chat.txt",'r')
txt=f.readlines()
names=[l.split()[0] for l in txt[::2]]
#[txt[l].split()[0] for l in range(len(txt)) if l%2==0]
# for line im lines[::2]:
print(names)
print("UNİQ : ",set(names)) #uniq names
f.close()

#Find the lendth of this chat :
f=open( "D:\\Personal\\Courses\\DCBootCamp\\dosyalar\\session3\\chat.txt",'r')
txt=f.readlines()
times=[l.split()[1] for l in txt[::2]]

start=int(times[0].split(":")[0])*60*60 +int(times[0].split(":")[1])*60 +int(times[0].split(":")[-1])
print( "*-*-*-*", start)

last=int(times[-1].split(":")[0])*3600 +int(times[-1].split(":")[1])*60 +int(times[-1].split(":")[-1])
print( "*-*-*-*", last)

print((last-start)/60)

print("++++++++",int(times[-1].split(":")[0]) - int(int(times[0].split(":")[0])))
f.close()
t_start=datetime.strptime(times[0],"%H:%M:%S")
t_last=datetime.strptime(times[-1],"%H:%M:%S")
print(t_last-t_start)


#Find the most active person in this chat :
#print(list(set([names.count(n) for n in names])))
print(names)