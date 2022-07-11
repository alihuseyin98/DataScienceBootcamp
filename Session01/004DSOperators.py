# OPERATİONS ON LİSTS-TUPLES-SETS

# LİSTS
l1=[1,2,3,4,5]
l2=[1,2,3,6,7,8,9]
print(set(l1+l2)) 
#print(l1+l2)
#print(l2-l1) #not accepted
#print(l1&l2) #not accepted
#print(l1|l2) #not accepted
#print(l1^l2) #not accepted

#SETS
s1={1,2,3,4,5}
s2={1,2,6,7,8,9}
s1[0]=10
print(type(s1))
#print(s1 & s2)
#print(s1 | s2)
#s1={"ali","huseyin"}
#s2={"salah","ali"}

#print(s1 + s2) # NOT ACCEPTED
print(s1 & s2) # both in a and b
print(s1 | s2) # all in a and b without repeat.
print(s1 - s2) # in a but not in b
print(s1 ^ s2) # in a but not in b - and in b but not in a
for x in s1:
    print(x)
print("Here ",(s1[:]))
#TUPLES
t1=(1,2,3,4,5)
t2=(1,2,6,7,8,9)
for x in t1:
    print(x)
print(t1[:])
print("--------------------",t1[0])
print(t1+t2)
#print(t1 & t2) # NOT ACCEPTED
#print(t1 | t2) # NOT ACCEPTED
#print(t1 - t2) # NOT ACCEPTED
#print(t1 ^ t2) # NOT ACCEPTED
