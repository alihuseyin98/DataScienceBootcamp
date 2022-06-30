import copy
l1=[[1,10,100],2,3,4,5]
l2=l1 #Shallow Copy
#l2=list(l1) #basic deep Copy
#l2=l1.copy() #basic deep Copy
#l2=copy.deepcopy(l1) #actual deep Copy
print(l1)
print(l2)
print("--------------")
l1[0][0]=500
print(l1)
print(l2)
print("--------------")
l1[0]=700
print(l1)
print(l2)
