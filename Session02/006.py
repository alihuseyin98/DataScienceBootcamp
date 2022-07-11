names=   ["ali","husein","salah","yousef"]
#one line loop
print(list("even" if x%2==0 else "odd" for x in range(10)))
# return  upper case list
#1 
l2=[]
for n in names :
    l2.append(n.upper()) 
print("#1 ",l2)
#2
l2=[]
count = 0
while (count<len(names)):
    l2.append(names[count].upper())
    count+=1
print("#2 ",l2)
#3
l2=[]
l2=[n.upper() for n in names ]
print("#3 ",l2)

#4
l2=[]
l2=list(map(lambda n:n.upper(),names))
print("#4 ",l2)