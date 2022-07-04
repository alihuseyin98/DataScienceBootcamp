#Shallow Copy (l2=l1) - Basic Deep Copy (l2=list(l1)) - Actual Deep Copy #import copy l2=copy.deepcopy(l1)
l1=[["ali","hamad"],"huseyin","yousef","salah"]
l2=list(l1)
print(l1)
print(l2)
l2[0][1]="ahmad"
print(l1)
print(l2)
s="hello"
print(s[0])