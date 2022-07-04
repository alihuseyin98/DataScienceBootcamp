#DİCTIONARİES
d2={(1,2):{"a":100,"b":50}}
for x in d2:
    print(d2[x])
    print((d2[x]["a"]+d2[x]["b"])/2)
    
d2={(1,2):{"a":100,"b":50}}
for x in d2.values():
    print("----",list(d2.values()))
    print((x["a"]+x["b"])/2)
    
    
print("---------------------------------------------------\n")
d1={"ali":100,"huseyin":99,"yousef":75}
print(d1.items())
for s in d1:
    print(str(d1[s])[0])
l1=[d1[x] for x in d1 ]
print(l1)

print(d1.values())
print(sum(d1.values())/3)

for k,v in d1.items():
    print(d1.items())
l=[((1,2),(3,4),(3,4),(3,4)),((5,6),(7,8),(3,4),(78,41)),((100,6),(7,8),(3,4),(78,41))]
for x,y,z,w in l:
    print(x,y,"-")
    
s={1,2,3,4}
t=(1,2,3,4,5)
l=[1,5,64,7,8,12,85]
i=iter(t)
print("next",next(i))
print(next(i))
print(next(i))
print(next(i))
print(list(i))