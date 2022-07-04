#DATA STRUCTURES PROPERTİES

#mutable, i.e., we can remove or add elements to it

#list : use index , diff. types , mutable , slice , iterable  : + *
#tuple : use index , diff. types , immutable , No change indix , slice , loop iterable : + *
#set : cant use index , diff. types , mutable , No change indix , loop iterable , not-slice : & | - ^
#dict : use keys , diff. types , mutable , not-iterable , not-slice

d={"a":1000,"b":2000}
for x in d:
    print(d[x])
    
    
t=(1,22,3)
print(type(t))
print(t[0])
l=[1,2]

print(type(l))
s={1,2,3}
#s[0]=1010
print(type(s))
print(t[0])

#ITERATER
i=iter(s)
print("iter ",next(i))
print(list(i))
for x in s:
    print("--", s)